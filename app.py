#!/usr/bin/env python3
"""
Provenance Guard — the web service.
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        audit.log_rejection(creator_id="unknown", reason="invalid_json_format")
        return jsonify({"error": "Invalid request format. Please send a valid JSON object."}), 400

    raw_creator = payload.get("creator_id")
    creator_id = raw_creator.strip() if isinstance(raw_creator, str) and raw_creator.strip() else "anonymous"

    if "text" not in payload:
        audit.log_rejection(creator_id=creator_id, reason="missing_text")
        return jsonify({"error": "Request must include a 'text' field."}), 400

    text = payload["text"]
    if not isinstance(text, str):
        audit.log_rejection(creator_id=creator_id, reason="non_string_text")
        return jsonify({"error": "The 'text' field must be text (a string), not a number or list."}), 400

    if not text.strip():
        audit.log_rejection(creator_id=creator_id, reason="empty_text")
        return jsonify({"error": "Your text is empty, please provide text."}), 400

    if len(text) > 10000:
        audit.log_rejection(creator_id=creator_id, reason="text_too_long")
        return jsonify({"error": "The text must be within 10,000 characters."}), 400

    content_id = str(uuid.uuid4())

    import detector
    import stylometry
    import scoring

    model_score = detector.model_signal(text)
    style_score = stylometry.style_signal(text)
    confidence = scoring.combine_signals(model_score, style_score)

    guess, label = scoring.score_to_label(confidence)

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        combined_score=confidence,
        label=label,
        status="decided",
    )

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": confidence,
        "label": label,
        "model_score": model_score,
        "style_score": style_score
    }), 200


@app.post("/appeal")
def appeal():
    payload = request.get_json(silent=True) or {}

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")
    creator_id = payload.get("creator_id", "unknown")

    if not content_id:
        audit.log_rejection(creator_id=str(creator_id), reason="missing_content_id_in_appeal")
        return jsonify({"error": "Missing content_id in request."}), 400

    if not audit.entries_for(content_id):
        return jsonify({"error": f"No record found for content_id: {content_id}"}), 404

    audit.log_appeal(
        content_id=content_id,
        creator_id=str(creator_id),
        reasoning=reasoning or "No reasoning provided."
    )

    return jsonify({
        "ok": True,
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been recorded and is now under review."
    }), 200


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
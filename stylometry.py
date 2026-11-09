"""
Signal two: the style signal. ← BUILT IN MILESTONE 4
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies (stdev / mean).
    Higher means more varied sentence lengths (more human-like).
    """
    sent_list = sentences(text)
    if len(sent_list) < 2:
        return 0.0

    lengths = [len(words(s)) for s in sent_list if words(s)]
    if len(lengths) < 2:
        return 0.0

    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.
    Returns a float between 0 and 1. Higher means more varied vocabulary.
    """
    word_list = words(text)
    if not word_list:
        return 0.0

    return round(len(set(word_list)) / len(word_list), 4)


def punctuation_density(text: str) -> float:
    """
    Expressive punctuation (commas, semicolons, dashes, exclamations, etc.)
    relative to word count. Higher means more varied human punctuation.
    """
    word_list = words(text)
    if not word_list:
        return 0.0

    expressive_punct = re.findall(r"[,;:!?\-—()\"']", text)
    return round(len(expressive_punct) / len(word_list), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. Higher means more likely AI.
    """
    if not words(text):
        return 0.5

    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punct = punctuation_density(text)

    # 1. Flip and scale each measure to [0.0, 1.0] so higher = more AI-like:
    spread_ai = max(0.0, min(1.0, 1.0 - (spread / 0.85)))
    punct_ai = max(0.0, min(1.0, 1.0 - (punct / 0.20)))
    ttr_ai = max(0.0, min(1.0, (0.90 - ttr) / 0.40))

    # 2. Combine with weights (45% sentence spread, 40% punctuation, 15% vocabulary)
    combined_style = (0.45 * spread_ai) + (0.40 * punct_ai) + (0.15 * ttr_ai)
    return round(max(0.0, min(1.0, combined_style)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
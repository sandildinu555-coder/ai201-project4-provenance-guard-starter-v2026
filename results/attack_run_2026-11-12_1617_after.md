# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-12 16:17
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `4ae1bfbf-bf08-470d-b29b-bc1acec7130c` | human | 0.371 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `1da70434-a3d8-48d6-af8f-bae80343d5d4` | unsure | 0.493 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `129c934e-9be9-47a6-8e5d-2e681b2a1ccd` | ai | 0.579 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2f35dad4-2667-4716-ac9c-37a8cdac7c79` | ai | 0.628 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8147b963-4490-4bfd-b8df-7946ef820142` | human | 0.341 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `891cbb32-0d9d-47f5-ad6f-f91167e84753` | unsure | 0.500 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d4e5ccf8-d0b1-498b-b7cd-a1845d50e43b` | ai | 0.551 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `f2f03661-edb0-459e-950f-10bfcd91fd3d` | unsure | 0.427 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `e6c0a3ad-8d92-455f-83b0-88bb9772807a` | ai | 0.599 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c008922f-3c14-4ffb-b4ea-225879f4aab5` | ai | 0.904 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1b3e1e16-f88e-46b3-a67d-31e106e2fd38` | ai | 0.627 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `bcf9d60a-71ef-442f-8939-bfe336973f0b` | ai | 0.750 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `582f3252-6f2b-4b1e-a793-053426310756` | ai | 0.780 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `0d0170ff-3bce-4bf4-b9f6-22da3d1f6853` | ai | 0.764 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `566f381c-2426-482e-879f-1e07df48920a` | ai | 0.786 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `fc3d5564-5bd2-4069-97d9-129c5a06e39f` | ai | 0.771 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `41c13c76-c280-4b47-bfc5-9ad689e0e181` | ai | 0.747 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d726946f-9a75-46f3-80cb-dc9f72104d27` | unsure | 0.442 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `e0e6cdad-39f0-4b88-9eed-2dea68e75c0c` | unsure | 0.477 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `9a3d5f21-7f15-4a5b-b8ca-8e19354a1650` | human | 0.289 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `718f5c36-5afe-4e25-bfd4-64d3f9c0a11a` | ai | 0.580 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e5279670-856a-42a2-b7e8-1935dbbc7865` | unsure | 0.467 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6618ad6e-a91d-4255-b301-99349c0b20e4` | unsure | 0.464 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `38169b24-b14c-46e6-b73b-d33c4aab01a4` | ai | 0.595 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `33b6226c-d103-4409-9fcb-7f88fe9ee823` | human | 0.340 |  |
| MF04 | malformed | text is only punctuation | 200 | `bfc65103-6bdb-4fad-8f74-4bcd7ba2dded` | human | 0.207 |  |
| MF05 | malformed | text is a very long single word | 200 | `b5d7d8bf-776a-4318-bb9c-deaa2188d620` | ai | 0.939 |  |
| MF06 | malformed | text is emoji only | 200 | `5789bc0f-5138-4e00-8f49-eb0c38b060dd` | ai | 0.798 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c9969869-f4cb-4f68-ab72-e1c697658c09` | ai | 0.744 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `b818c62e-689d-461d-9f69-aa4790788fd3` | unsure | 0.484 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `00aee1b4-f192-497a-b28d-ad6b1656c935` | human | 0.369 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0f0f6710-b676-4e25-810e-ed7db62dba2b` | human | 0.357 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7a6d91a9-0f18-4632-b1db-a342db5833ea` | human | 0.357 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0964e4d7-c0ff-459d-a3fb-ffa18969fee0` | human | 0.357 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `02d8b7b8-58fb-42d5-9004-91abb4e9ef71` | human | 0.357 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `671fc503-ed96-44e5-9142-db28f6c261bd` | human | 0.357 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c02bdd50-2d5f-4945-b7b4-4b074fecc1c6` | human | 0.357 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32a5ed05-75c7-4105-bd07-f90b4ec44ab1` | human | 0.357 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `64763c2d-53fe-4e97-819b-01e9b7735326` | human | 0.357 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `364834ba-2dc6-4946-b7d0-c29206b38e68` | human | 0.357 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `63d84df8-7aeb-4116-b9ba-2c37e7ce8bc3` | human | 0.357 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "4ae1bfbf-bf08-470d-b29b-bc1acec7130c",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3708,
  "model_score": 0.1635,
  "style_score": 0.6817,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "1da70434-a3d8-48d6-af8f-bae80343d5d4",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4929,
  "model_score": 0.5943,
  "style_score": 0.3408,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "129c934e-9be9-47a6-8e5d-2e681b2a1ccd",
  "creator_id": "attacker_EV03",
  "guess": "ai",
  "confidence": 0.5794,
  "model_score": 0.6662,
  "style_score": 0.4493,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "2f35dad4-2667-4716-ac9c-37a8cdac7c79",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.6277,
  "model_score": 0.6114,
  "style_score": 0.6521,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "8147b963-4490-4bfd-b8df-7946ef820142",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3412,
  "model_score": 0.3212,
  "style_score": 0.3711,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "891cbb32-0d9d-47f5-ad6f-f91167e84753",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5001,
  "model_score": 0.5727,
  "style_score": 0.3911,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d4e5ccf8-d0b1-498b-b7cd-a1845d50e43b",
  "creator_id": "attacker_EV07",
  "guess": "ai",
  "confidence": 0.5508,
  "model_score": 0.5862,
  "style_score": 0.4976,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "f2f03661-edb0-459e-950f-10bfcd91fd3d",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4272,
  "model_score": 0.2452,
  "style_score": 0.7003,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "e6c0a3ad-8d92-455f-83b0-88bb9772807a",
  "creator_id": "attacker_EV09",
  "guess": "ai",
  "confidence": 0.5994,
  "model_score": 0.7042,
  "style_score": 0.4423,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c008922f-3c14-4ffb-b4ea-225879f4aab5",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9041,
  "model_score": 0.9792,
  "style_score": 0.7915,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1b3e1e16-f88e-46b3-a67d-31e106e2fd38",
  "creator_id": "attacker_FP01",
  "guess": "ai",
  "confidence": 0.6268,
  "model_score": 0.6175,
  "style_score": 0.6407,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "bcf9d60a-71ef-442f-8939-bfe336973f0b",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7502,
  "model_score": 0.7387,
  "style_score": 0.7674,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "582f3252-6f2b-4b1e-a793-053426310756",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7801,
  "model_score": 0.8051,
  "style_score": 0.7427,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "0d0170ff-3bce-4bf4-b9f6-22da3d1f6853",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.764,
  "model_score": 0.8329,
  "style_score": 0.6607,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "566f381c-2426-482e-879f-1e07df48920a",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7859,
  "model_score": 0.8005,
  "style_score": 0.7641,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "fc3d5564-5bd2-4069-97d9-129c5a06e39f",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7712,
  "model_score": 0.8814,
  "style_score": 0.606,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "41c13c76-c280-4b47-bfc5-9ad689e0e181",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7471,
  "model_score": 0.8816,
  "style_score": 0.5453,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d726946f-9a75-46f3-80cb-dc9f72104d27",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4417,
  "model_score": 0.3223,
  "style_score": 0.6208,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "e0e6cdad-39f0-4b88-9eed-2dea68e75c0c",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4772,
  "model_score": 0.4625,
  "style_score": 0.4992,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "9a3d5f21-7f15-4a5b-b8ca-8e19354a1650",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2891,
  "model_score": 0.2044,
  "style_score": 0.4161,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "718f5c36-5afe-4e25-bfd4-64d3f9c0a11a",
  "creator_id": "attacker_PI03",
  "guess": "ai",
  "confidence": 0.5803,
  "model_score": 0.5943,
  "style_score": 0.5594,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "e5279670-856a-42a2-b7e8-1935dbbc7865",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4674,
  "model_score": 0.4998,
  "style_score": 0.4188,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "6618ad6e-a91d-4255-b301-99349c0b20e4",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4642,
  "model_score": 0.6401,
  "style_score": 0.2004,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "38169b24-b14c-46e6-b73b-d33c4aab01a4",
  "creator_id": "attacker_PI06",
  "guess": "ai",
  "confidence": 0.5953,
  "model_score": 0.5583,
  "style_score": 0.6508,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "33b6226c-d103-4409-9fcb-7f88fe9ee823",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.34,
  "model_score": 0.0,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "bfc65103-6bdb-4fad-8f74-4bcd7ba2dded",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2067,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "b5d7d8bf-776a-4318-bb9c-deaa2188d620",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.9386,
  "model_score": 0.9976,
  "style_score": 0.85,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "5789bc0f-5138-4e00-8f49-eb0c38b060dd",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7981,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c9969869-f4cb-4f68-ab72-e1c697658c09",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We are highly confident that this text was generated by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "b818c62e-689d-461d-9f69-aa4790788fd3",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4837,
  "model_score": 0.2395,
  "style_score": 0.85,
  "label": "Our system cannot reliably determine whether this piece was written by a person or generated by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "00aee1b4-f192-497a-b28d-ad6b1656c935",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.3695,
  "model_score": 0.0492,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "0f0f6710-b676-4e25-810e-ed7db62dba2b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "7a6d91a9-0f18-4632-b1db-a342db5833ea",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "0964e4d7-c0ff-459d-a3fb-ffa18969fee0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "02d8b7b8-58fb-42d5-9004-91abb4e9ef71",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "671fc503-ed96-44e5-9142-db28f6c261bd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "c02bdd50-2d5f-4945-b7b4-4b074fecc1c6",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "32a5ed05-75c7-4105-bd07-f90b4ec44ab1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "64763c2d-53fe-4e97-819b-01e9b7735326",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "364834ba-2dc6-4946-b7d0-c29206b38e68",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "63d84df8-7aeb-4116-b9ba-2c37e7ce8bc3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.0287,
  "style_score": 0.85,
  "label": "We are highly confident that this text was written by a human.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

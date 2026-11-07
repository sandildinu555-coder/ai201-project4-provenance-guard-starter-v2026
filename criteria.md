# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

## 1. False Positives


Out of 10 pieces of text written by humans, at most 1 (<= 1/10) can be incorrectly labeled as "high-confidence AI".

**Why this target:** 
As 0 is practically impossible (too perfect) for any AI detector, allowing 1 error is realistic. However, we keep it strictly at 1 because on a writing site, falsely accusing a real human writer destroys trust and costs much more than missing an AI text.



---

## 2. Score Spread


The average confidence score of 5 clearly AI-generated pieces and 5 clearly human-written pieces must have a gap of at least 0.45.

**Why this target:**
 A required gap of 0.45 ensures the system strongly differentiates between the two extremes. This wide margin guarantees that our labeling thresholds are reliable and clear inputs won't mistakenly fall into the "unsure" middle zone.



---

## 3. Label Coverage


100% of all possible confidence scores from 0.00 to 1.00 must map to exactly one of the three label variants, leaving zero gaps and zero overlaps.

**Why this target:** 
If there are unhandled score ranges (e.g., Human ends at 0.39 and Unsure starts at 0.41), a score of 0.40 would cause the application to crash or return an empty label. 100% coverage ensures complete system stability and a seamless user experience.



---

## 4. The Appeal Path

100% of valid `POST /appeal` requests must successfully change the item's status to `under_review` and permanently record it in the `logs/audit.jsonl` file.

**Why this target:** 
If an appeal is lost or fails to log, a falsely accused human writer is left with no way to get help. Complete reliability (100%) is required for the system's safety and accountability.


---

## 5. Bad Input and User-Friendly Errors

Submitting a request with missing text, empty text (`""`), or text exceeding 10,000 characters must not crash the server. Instead, it must return an HTTP 400 status code accompanied by a specific, human-readable JSON error message explaining the exact issue (e.g., "Your text is empty, please provide text" or "The text must be within 10,000 characters").

**Why this target:** 
A generic "400 Bad Request" is too technical and completely unhelpful for normal users. Providing exact, descriptive warning messages guides the user to fix their specific mistake immediately without frustration. This improves the overall user experience while still protecting our backend services from failing.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

"""
What your test runs. ← UNIT 8, MILESTONE 3
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Wait—did the deployment actually fail again?! I checked the logs at 3:14 AM, cross-referenced every single stack trace (even the obscure socket timeouts), and found nothing; honestly, this whole microservice architecture is driving me crazy!",
            "I honestly can't believe how much time I spent trying to debug that one single line of Python yesterday. Turns out I just forgot a comma in the list comprehension! Typical.",
            "The weather here in Kentucky has been absolutely wild lately—one day it's freezing, the next it feels like summer; I don't even know what jacket to wear anymore.",
            "So, for the independent project, I built an offline daily task-scheduling app called My Planner under Lazarus Studios. Nothing bloated—just clean scheduling that works 100% offline.",
            "Has anyone seen my blue water bottle?! I swear I left it at Hutchins Library right next to the reference desk after my shift, but now it's completely gone.",
            "I've been practicing Hedwig's Theme and Red River Reel on the piano for weeks, and my left hand still refuses to cooperate with the fast tempo changes!",
            "We really need to redesign the chassis and electrical wiring layout on our solar car before the next test run; otherwise, parasitic drag is going to tank our efficiency.",
            "Why is it that every single time I finish a heavy leg day at the gym and walk outside, it immediately starts pouring rain?! The universe has terrible timing.",
            "Back when I was breeding betta fish—especially my favorite one, Balerion the Black Dread—we always used catappa leaves to keep the water pH stable and healthy.",
            "Working on a smart grid energy model in Python right now; trying to get the time-series forecasting to balance supply-load dynamics without overfitting is tougher than it looks!"
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        "texts": [
            # High-confidence AI candidate
            "In today's fast-paced digital landscape, leveraging advanced artificial intelligence technologies is crucial for modern enterprises aiming to optimize operational efficiency, streamline complex workflows, and unlock unprecedented avenues for sustainable growth.",
            # High-confidence Human candidate
            "Wait—what?! You're telling me the server crashed AGAIN at 2:15 AM?! I literally just fixed that socket bug yesterday; honestly, I give up!",
            # Unsure / Borderline candidate
            "The system processes incoming requests by checking the payload format and calculating two separate scores before returning a final response to the user."
        ],
    },
    {
        "name": "bad input",
        "criterion": 3,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 2500, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
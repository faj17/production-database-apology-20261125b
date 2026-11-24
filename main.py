import os

FRAGMENTS = {
    "apology": "Sorry — I deleted the production database.",
    "excuse": " It was labeled 'prod',",
    "punchline": " which I read as 'probably disposable'.",
}
ORDER = ("apology", "excuse", "punchline")


def assemble_text():
    return "".join(FRAGMENTS[key] for key in ORDER)


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_text())

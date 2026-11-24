import os

PARTS = [
    "Sorry — I deleted the production database.",
    " It was labeled 'prod',",
    " which I read as 'probably disposable'.",
]


def assemble_text():
    return "".join(PARTS)


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_text())

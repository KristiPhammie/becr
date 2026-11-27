from pathlib import Path
import re

README = Path("README.md")

# discover models
hmm_files = {
    p.stem: p.name
    for p in sorted(Path("hmm").glob("*.hmm"))
}

hhm_files = {
    p.stem: p.name
    for p in sorted(Path("hhm").glob("*.hhm"))
}

text = README.read_text()

# ------------------------------------------------------------------
# Add Model column to tables
# ------------------------------------------------------------------

lines = text.splitlines()
new_lines = []

for i, line in enumerate(lines):

    if (
        line.startswith("| Toxin Family")
        and "Model" not in line
        and "Alignment" in line
    ):
        line = line.replace(
            "Alignment | Annotated Structure",
            "Alignment | Model | Annotated Structure"
        )

    elif (
        line.startswith("|---")
        and i > 0
        and "Model" in lines[i - 1]
        and line.count("|") == 5
    ):
        parts = line.split("|")
        line = (
            "|" +
            parts[1] +
            "|" +
            parts[2] +
            "|" +
            parts[3] +
            "|------" +
            "|" +
            parts[4] +
            "|"
        )

    elif (
        line.startswith("|")
        and not line.startswith("| Toxin Family")
        and "Annotated Structure" not in line
    ):
        cols = [c.strip() for c in line.split("|")[1:-1]]

        if len(cols) == 4:

            family = cols[0]

            ref = re.sub(r"<.*?>", "", family)
            ref = ref.replace("[", "").replace("]", "")

            model_links = []

            if ref in hmm_files:
                model_links.append(f"[hmm][{ref}_hmm]")

            if ref in hhm_files:
                model_links.append(f"[hhm][{ref}_hhm]")

            model_col = " ".join(model_links)

            line = (
                f"| {cols[0]} | {cols[1]} | {cols[2]} | "
                f"{model_col} | {cols[3]} |"
            )

    new_lines.append(line)

text = "\n".join(new_lines)

# ------------------------------------------------------------------
# Append model sections
# ------------------------------------------------------------------

text += "\n\n## HMM Models\n\n"

for stem, fname in sorted(hmm_files.items()):
    text += f"- [{fname}][{stem}_hmm]\n"

text += "\n## HHM Models\n\n"

for stem, fname in sorted(hhm_files.items()):
    text += f"- [{fname}][{stem}_hhm]\n"

text += "\n\n"

# ------------------------------------------------------------------
# Append reference link definitions
# ------------------------------------------------------------------

for stem, fname in sorted(hmm_files.items()):
    text += (
        f"[{stem}_hmm]: "
        f"https://raw.githubusercontent.com/KristiPhammie/becr/main/hmm{fname}\n"
    )

for stem, fname in sorted(hhm_files.items()):
    text += (
        f"[{stem}_hhm]: "
        f"https://raw.githubusercontent.com/KristiPhammie/becr/main/hhm{fname}\n"
    )

README.write_text(text)

print(f"Added {len(hmm_files)} HMM links")
print(f"Added {len(hhm_files)} HHM links")
import re
from pathlib import Path

def normalize_text(text: str) -> str:
    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text)
    # Fix broken "Opponents"
    text = text.replace("O p p o n e n t s", "Opponents")
    return text

def parse_goals(raw_text_file):
    text = Path(raw_text_file).read_text(encoding="utf-8")

    # Grab the block
    match = re.search(r"Goals by Period(.+?)Saves by Period", text, re.S | re.IGNORECASE)
    if not match:
        raise ValueError("Could not find 'Goals by Period' section in text.")
    goals_block = normalize_text(match.group(1))

    # Save debug version
    Path("outputs/goals_block_debug.txt").write_text(goals_block, encoding="utf-8")

    # Find all numbers in Syracuse row
    syr_match = re.search(r"Syracuse\s+([\d\s]+)", goals_block, re.IGNORECASE)
    opp_match = re.search(r"Opponents\s+([\d\s]+)", goals_block, re.IGNORECASE)

    if not syr_match or not opp_match:
        raise ValueError("Could not parse Syracuse or Opponents rows. See outputs/goals_block_debug.txt")

    syracuse_nums = [int(x) for x in syr_match.group(1).split() if x.isdigit()]
    opponents_nums = [int(x) for x in opp_match.group(1).split() if x.isdigit()]

    # Only keep first 5 (1st–OT)
    syracuse_nums = syracuse_nums[:5]
    opponents_nums = opponents_nums[:5]

    periods = ["1st", "2nd", "3rd", "4th", "OT"]
    parsed = [(p, syracuse_nums[i], opponents_nums[i]) for i, p in enumerate(periods)]

    return parsed

if __name__ == "__main__":
    data = parse_goals("outputs/2024SUStats_raw.txt")
    print(data)

import re
import sys
from pathlib import Path


def set_class_name(content: str, name: str) -> str:
    return re.sub(r"\bSolution\d*\b", name, content)


if len(sys.argv) < 2:
    print("Usage: swap_solution.py <filename>  (e.g. solution2.py)")
    sys.exit(1)

other = Path(sys.argv[1])
base = Path("solution.py")

if not other.exists():
    print(f"{other} not found")
    sys.exit(1)

if other.name == base.name:
    print("Already solution.py")
    sys.exit(0)

suffix = re.search(r"\d+", other.stem)
other_class = f"Solution{suffix.group()}" if suffix else "Solution"

base_content = set_class_name(base.read_text(), other_class)
other_content = set_class_name(other.read_text(), "Solution")

base.write_text(other_content)
other.write_text(base_content)
print(f"Swapped {base.name} <-> {other.name}")

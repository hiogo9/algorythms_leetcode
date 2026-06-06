import re
import sys
from pathlib import Path


def rename_class(content: str, name: str) -> str:
    return re.sub(r"\bSolution\d*\b", name, content)


if len(sys.argv) < 2:
    print("Usage: swap_solution.py <filename>  (e.g. solution2.py)")
    sys.exit(1)

other = Path(sys.argv[1])
base = Path("solution.py")

if other.name == base.name:
    print("Already solution.py")
    sys.exit(0)

if not other.exists():
    available = ", ".join(p.name for p in sorted(Path(".").glob("solution[0-9]*.py")))
    print(f"{other} not found. Available: {available or 'none'}")
    sys.exit(1)

suffix = re.search(r"\d+", other.stem)
other_class = f"Solution{suffix.group()}" if suffix else "Solution"

base_text, other_text = base.read_text(), other.read_text()
base.write_text(rename_class(other_text, "Solution"))
other.write_text(rename_class(base_text, other_class))
print(f"Swapped {base.name} <-> {other.name}")

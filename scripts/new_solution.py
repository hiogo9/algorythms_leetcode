import re
import subprocess
import sys
from pathlib import Path

BASE = Path("solution.py")

if not BASE.exists():
    print("solution.py not found in current directory")
    sys.exit(1)


def next_slot() -> int:
    n = 2
    while Path(f"solution{n}.py").exists():
        n += 1
    return n


def make_stub(content: str) -> str:
    return re.sub(
        r"(    def [^\n]+:\n).*?(\n# @lc code=end)",
        r"\1        pass\n\2",
        content,
        flags=re.DOTALL,
    )


n = next_slot()
dest = Path(f"solution{n}.py")

# Move solution.py → solutionN.py with renamed class
content = BASE.read_text()
dest.write_text(re.sub(r"\bSolution\b", f"Solution{n}", content))

# Add test block for solutionN (reuses gen_test.py logic)
scripts_dir = Path(__file__).parent
subprocess.run([sys.executable, scripts_dir / "gen_test.py"], check=True)

# Create new empty solution.py — full copy with method body replaced by pass
BASE.write_text(make_stub(content))

print(f"solution.py archived to {dest.name}, new solution.py ready")

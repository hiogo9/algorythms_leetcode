import re
import sys
from pathlib import Path

solution = Path("solution.py")
test_file = Path("test_solution.py")

if not solution.exists():
    print("solution.py not found in current directory")
    sys.exit(1)

if test_file.exists():
    print("test_solution.py already exists")
    sys.exit(1)

content = solution.read_text()
match = re.search(r"def (\w+)\(self", content)
method = match.group(1) if match else "methodName"

test_file.write_text(f"""import pytest
from solution import Solution

@pytest.mark.parametrize("args, expected", [
    ((), ),
])
def test_solution(args, expected):
    assert Solution().{method}(*args) == expected
""")

print(f"Created test_solution.py (method: {method})")

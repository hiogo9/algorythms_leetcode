import re
import sys
from pathlib import Path


def class_name(sol_path: Path) -> str:
    suffix = sol_path.stem[len("solution") :]
    return f"Solution{suffix}"


def solution_files() -> list[Path]:
    files = [Path("solution.py")] + sorted(Path(".").glob("solution[0-9]*.py"))
    return [f for f in files if f.exists()]


def prepare_solution(sol_path: Path) -> None:
    content = sol_path.read_text()
    cls = class_name(sol_path)

    if "from typing import" not in content:
        content = content.replace(
            "class Solution", "from typing import *\nclass Solution", 1
        )

    if cls != "Solution" and f"class {cls}" not in content:
        content = re.sub(r"\bSolution\d*\b", cls, content)

    sol_path.write_text(content)


def get_method(sol_path: Path) -> str:
    match = re.search(r"def (\w+)\(self", sol_path.read_text())
    return match.group(1) if match else "methodName"


def extract_cases(test_path: Path) -> str:
    content = test_path.read_text()
    m = re.search(r'@pytest\.mark\.parametrize\(\s*"args, expected",\s*', content)
    if not m:
        return "[\n        ((), ),\n    ],"
    start = content.index("[", m.end())
    depth = 0
    for i, ch in enumerate(content[start:], start):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                tail = "," if content[i + 1 : i + 2] == "," else ""
                return content[start : i + 1] + tail
    return "[\n        (( ,), ),\n    ],"


def test_block(sol_path: Path, method: str, cases: str) -> str:
    cls = class_name(sol_path)
    fn = f"test_{sol_path.stem}"
    return f"""
@pytest.mark.parametrize(
    "args, expected",
    {cases}
)
def {fn}(args, expected):
    assert {cls}().{method}(*args) == expected
"""


if not Path("solution.py").exists():
    print("solution.py not found in current directory")
    sys.exit(1)

solutions = solution_files()
for sol in solutions:
    prepare_solution(sol)

method = get_method(Path("solution.py"))
test_file = Path("test_solution.py")

if not test_file.exists():
    imports = "\n".join(f"from {s.stem} import {class_name(s)}" for s in solutions)
    cases = "[\n        ((), ),\n    ],"
    blocks = "".join(test_block(s, method, cases) for s in solutions)
    test_file.write_text(f"import pytest\n{imports}\n{blocks}")
    print(f"Created test_solution.py (method: {method})")
else:
    existing = test_file.read_text()
    cases = extract_cases(test_file)
    added = []
    for sol in solutions:
        if f"from {sol.stem} import" not in existing:
            existing = f"from {sol.stem} import {class_name(sol)}\n" + existing
            existing += test_block(sol, method, cases)
            added.append(class_name(sol))
    if added:
        test_file.write_text(existing)
        print(f"Added to test_solution.py: {', '.join(added)}")
    else:
        print("All solutions already in test_solution.py")

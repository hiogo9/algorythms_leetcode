import re
import sys
from pathlib import Path


def ensure_typing_import(sol_path: Path) -> None:
    content = sol_path.read_text()
    if "from typing import" not in content:
        lines = content.splitlines(keepends=True)
        insert_at = next(
            (i for i, l in enumerate(lines) if l.startswith("class Solution")),
            0,
        )
        lines.insert(insert_at, "from typing import *\n")
        sol_path.write_text("".join(lines))


def get_method(sol_path: Path) -> str:
    match = re.search(r"def (\w+)\(self", sol_path.read_text())
    return match.group(1) if match else "methodName"


def solution_files() -> list[Path]:
    here = Path(".")
    files = sorted(
        [Path("solution.py")]
        + sorted(here.glob("solution[0-9]*.py")),
        key=lambda p: p.name,
    )
    return [f for f in files if f.exists()]


def class_name(sol_path: Path) -> str:
    stem = sol_path.stem  # solution, solution2, solution3...
    suffix = stem[len("solution"):]
    return f"Solution{suffix.upper() if suffix else ''}" if not suffix else f"Solution{suffix}"


def extract_cases(test_path: Path) -> str:
    match = re.search(
        r'@pytest\.mark\.parametrize\(\s*"args, expected",\s*(\[.*?\],)',
        test_path.read_text(),
        re.DOTALL,
    )
    return match.group(1) if match else "[\n        ((), ),\n    ],"


def test_block(sol_path: Path, method: str, cases: str) -> str:
    cls = class_name(sol_path)
    stem = sol_path.stem
    fn = f"test_{stem}"
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

test_file = Path("test_solution.py")
solutions = solution_files()

for sol in solutions:
    ensure_typing_import(sol)

method = get_method(Path("solution.py"))

if not test_file.exists():
    imports = "\n".join(
        f"from {s.stem} import {class_name(s)}" for s in solutions
    )
    cases = "[\n        ((), ),\n    ],"
    blocks = "".join(test_block(s, method, cases) for s in solutions)
    test_file.write_text(f"import pytest\n{imports}\n{blocks}")
    print(f"Created test_solution.py (method: {method})")
else:
    existing = test_file.read_text()
    cases = extract_cases(test_file)
    added = []
    for sol in solutions:
        cls = class_name(sol)
        if f"from {sol.stem} import" not in existing:
            import_line = f"from {sol.stem} import {cls}\n"
            existing = import_line + existing
            existing += test_block(sol, method, cases)
            added.append(cls)
    if added:
        test_file.write_text(existing)
        print(f"Added to test_solution.py: {', '.join(added)}")
    else:
        print("All solutions already in test_solution.py")

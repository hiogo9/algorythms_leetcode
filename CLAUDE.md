# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
.venv/bin/pytest problems/ -v               # run all tests
.venv/bin/pytest problems/1_two_sum/ -v     # single problem
```

## Structure

Each problem: `problems/{id}_{name}/solution.py` + `test_solution.py`.

`problems/conftest.py` injects `List`, `Optional`, `Dict`, `Set`, `Tuple`, `ListNode`, `TreeNode` into builtins. `ListNode`/`TreeNode` have `.from_list()` / `.to_list()` helpers.

## Key rules

- Folder names start with a digit → invalid Python identifiers → no `__init__.py`, no relative imports. Always use `from solution import Solution`.
- Solution methods need a trailing `return []` / `return None` to satisfy Pylance even when LeetCode guarantees a result.
- F5 debug: `test_solution.py` must be the active tab (breakpoints can be in `solution.py`).

## Test template

```python
import pytest
from solution import Solution


@pytest.mark.parametrize(
    "args, expected",
    [
        (([2, 7, 11, 15], 9), [0, 1]),
    ],
)
def test_solution(args, expected):
    assert Solution().twoSum(*args) == expected
```

## Commit convention

```
feat: solved [problem number]
```

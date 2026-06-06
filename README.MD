# LeetCode / Python

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### VS Code extensions

1. Extensions (Ctrl+Shift+X) → install **LeetCode** (by LeetCode).
2. Ctrl+Shift+P → **LeetCode: Sign In** → LeetCode.com → Cookie.
3. Ctrl+Shift+P → **Open User Settings (JSON)** → add:

```json
"leetcode.useWsl": true,
"leetcode.defaultLanguage": "python3",
"leetcode.workspaceFolder": "/mnt/c/python_projects/algorythms_leetcode",
"leetcode.filePath": {
    "python3": {
        "folder": "problems",
        "filename": "${id}_${snakeCaseName}/solution.py"
    }
}
```

---

## Workflow

### 1. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 2. Open a problem

Sidebar → LeetCode → select a problem. The extension creates `problems/{id}_{name}/solution.py`.

### 2. Create a test

Run **Tasks: Run Task → Generate Test File**, or create `test_solution.py` manually. Type `lctest` + Tab:

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

### 3. Run tests

Testing panel in the sidebar (beaker icon) → click ▶ next to a test, file, or folder.

Or from the terminal:

```bash
.venv/bin/pytest problems/ -v
.venv/bin/pytest problems/1_two_sum/ -v
```

### 4. Debug

Set a breakpoint in `solution.py`, open `test_solution.py`, press **F5**.

### 5. Submit and commit

Ctrl+Shift+P → **LeetCode: Submit** → if Accepted:



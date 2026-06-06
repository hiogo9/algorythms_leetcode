# Create the project directory and initialize Git
```bash
mkdir algorythms_leetcode && cd algorythms_leetcode
git init
git branch -M main
```
# Create base directories
```bash
mkdir problems
mkdir .vscode
```
# Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
# Install and freeze dependencies
```bash
pip install --upgrade pip
pip install pytest
echo "pytest" > requirements.txt
```

Open VS Code.

1. Go to Extensions (Ctrl+Shift+X) and install the LeetCode extension (by shengchen or LeetCode).

2. Sign in: Ctrl+Shift+P -> LeetCode: Sign In -> LeetCode.com -> Cookie (copy cookies from your browser).

3. Open Global Settings: Press Ctrl+Shift+P -> type Open User Settings (JSON).

4. Add the following lines to the bottom of your global settings.json file. Make sure to replace the path with your actual WSL absolute path:
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



1. .gitignore

(In the root of the project)
```gitignore
# Virtual environment
.venv/

# Python cache
__pycache__/
*.py[cod]
*$py.class

# Pytest cache
.pytest_cache/

# System files
.DS_Store
```

2. Makefile

(In the root of the project)
```makefile
.PHONY: setup test clean

setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

test:
	.venv/bin/pytest problems/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
```

3. .vscode/launch.json

Allows you to start the debugger by pressing F5 specifically for the currently opened test file.
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug Current Test",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "${file}",
                "-v"
            ],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

4. .vscode/leetcode.code-snippets

A custom snippet to instantly generate a test boilerplate. Type lctest in your test file and press Tab.
```json
{
    "LeetCode Pytest": {
        "scope": "python",
        "prefix": "lctest",
        "body": [
            "import pytest",
            "from .solution import Solution",
            "",
            "@pytest.mark.parametrize(\"args, expected\", [",
            "    (($1), $2),",
            "])",
            "def test_solution(args, expected):",
            "    assert Solution().$3(*args) == expected"
        ],
        "description": "Generate Pytest block for LeetCode"
    }
}
```

5. problems/conftest.py

Global pytest configuration. It injects typing and LeetCode data structures globally so you don't have to import them in every single solution. (Note: Added # type: ignore to suppress Pylance warnings).

```python
import builtins
import collections
from typing import List, Optional, Dict, Set, Tuple, Deque

# Глобальная инъекция типов
for t in (List, Optional, Dict, Set, Tuple):
    setattr(builtins, t.__name__, t)

# Связный список
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr: Optional[List[int]]) -> Optional['ListNode']:
        if not arr: 
            return None
        head = cls(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = cls(val)
            curr = curr.next
        return head

    def to_list(self) -> List[int]:
        res: List[int] = []
        curr: Optional['ListNode'] = self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


# Бинарное дерево
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr: Optional[List[Optional[int]]]) -> Optional['TreeNode']:
        if not arr or arr[0] is None: 
            return None
            
        root = cls(arr[0])
        # Явно указываем Pylance, что очередь содержит только узлы дерева
        queue: Deque['TreeNode'] = collections.deque([root])
        i = 1
        
        while queue and i < len(arr):
            node = queue.popleft()
            
            # Левый потомок
            if i < len(arr) and arr[i] is not None:
                # Создаем узел, сохраняем в переменную (у неё точный тип)
                left_child = cls(arr[i]) # type: ignore
                node.left = left_child
                queue.append(left_child) # Pylance теперь видит четкий тип
            i += 1
            
            # Правый потомок
            if i < len(arr) and arr[i] is not None:
                right_child = cls(arr[i]) # type: ignore
                node.right = right_child
                queue.append(right_child)
            i += 1
            
        return root

    def to_list(self) -> List[Optional[int]]:
        if not self: 
            return []
            
        result: List[Optional[int]] = []
        queue: Deque[Optional['TreeNode']] = collections.deque([self])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
                
        # LeetCode обрезает пустые узлы (None) в конце массива
        while result and result[-1] is None:
            result.pop()
            
        return result

# Подавляем ошибку присваивания в builtins
builtins.ListNode = ListNode  # type: ignore
builtins.TreeNode = TreeNode  # type: ignore
```

Commit the baseline configuration to Git:
```bash
git add .
git commit -m "chore: setup leetcode environment"
```

Phase 3: Daily Workflow

1. Fetch a Problem

Click the LeetCode icon in the VS Code sidebar.

Select a problem (ensure the language is set to Python3).

The extension will automatically create problems/PROBLEM_NAME/solution.py using your global settings.

2. Write Tests

Create a file named test_solution.py next to the solution.py file.

Type lctest and press Tab to expand the snippet.

Copy the Input/Output from the problem description and paste it into the @pytest.mark.parametrize array.
(If the problem requires ListNode or TreeNode, import them from problems.conftest and use .from_list() / .to_list() inside the test).

3. Solve & Verify

Implement your logic in solution.py.

Open the integrated terminal (Ctrl + ~) and run:
```bash
make test
```

4. Debug (If tests fail)

Open solution.py and click to the left of the line numbers to set a red breakpoint.

Switch back to test_solution.py (it must be the active tab).

Press F5.

The debugger will pause at your breakpoint. Use the Variables panel on the left or the Debug Console at the bottom to inspect data.

Controls: F10 (Step Over), F11 (Step Into), F5 (Continue).

For Trees/Lists: In the Debug Console, type variable.to_list() to print the object as a standard array.

5. Submit & Commit

Press Ctrl+Shift+P -> LeetCode: Submit.

If the result is Accepted:
```bash
git add problems/PROBLEM_NAME
git commit -m "feat: solved [problem number]"
git push
```

#test example
```python
import pytest
from .solution import Solution

# If the problem uses ListNode or TreeNode, import them like this:
# from problems.conftest import ListNode, TreeNode

@pytest.mark.parametrize("args, expected", [
    # Test Case 1: Standard input from LeetCode
    # args: (array of numbers, target number)
    (([2, 7, 11, 15], 9), [0, 1]),
    
    # Test Case 2
    (([3, 2, 4], 6), [1, 2]),
    
    # Test Case 3
    (([3, 3], 6), [0, 1])
])
def test_solution(args, expected):
    # 'args' is unpacked using *args
    # Replace 'twoSum' with the actual method name of your Solution
    assert Solution().twoSum(*args) == expected

# ---------------------------------------------------------
# EXAMPLE FOR LINKED LIST (e.g., Reverse Linked List)
# ---------------------------------------------------------
#
# @pytest.mark.parametrize("arr_in, arr_expected", [
#     ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
#     ([], []),
# ])
# def test_reverse_list(arr_in, arr_expected):
#     # 1. Deserialize the array into ListNode objects
#     head = ListNode.from_list(arr_in)
#     
#     # 2. Run the solution
#     result_node = Solution().reverseList(head)
#     
#     # 3. Serialize the result back into an array for comparison
#     result_arr = result_node.to_list() if result_node else []
#     assert result_arr == arr_expected
```
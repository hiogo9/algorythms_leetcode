import sys
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


from _pytest.python import Module


class SolutionModule(Module):
    def collect(self):
        path_str = str(self.path.parent)
        sys.modules.pop("solution", None)
        if path_str in sys.path:
            sys.path.remove(path_str)
        sys.path.insert(0, path_str)
        return super().collect()


def pytest_collect_file(parent, file_path):
    if file_path.name == "test_solution.py":
        return SolutionModule.from_parent(parent, path=file_path)
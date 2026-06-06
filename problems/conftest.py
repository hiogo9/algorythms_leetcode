import builtins
import collections
from typing import List, Optional, Dict, Set, Tuple

# Глобальная инъекция типов
for t in (List, Optional, Dict, Set, Tuple):
    setattr(builtins, t.__name__, t)

# Связный список
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, arr):
        if not arr: return None
        head = cls(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = cls(val)
            curr = curr.next
        return head

    def to_list(self):
        res, curr = [], self
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

# Бинарное дерево
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, arr):
        if not arr: return None
        root = cls(arr[0])
        queue = collections.deque([root])
        i = 1
        while queue and i < len(arr):
            node = queue.popleft()
            if i < len(arr) and arr[i] is not None:
                node.left = cls(arr[i])
                queue.append(node.left)
            i += 1
            if i < len(arr) and arr[i] is not None:
                node.right = cls(arr[i])
                queue.append(node.right)
            i += 1
        return root

    def to_list(self):
        if not self: return []
        result = []
        queue = collections.deque([self])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result

builtins.ListNode = ListNode
builtins.TreeNode = TreeNode
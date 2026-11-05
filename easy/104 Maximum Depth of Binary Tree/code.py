# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depths = 0

        if root is None:
            return 0

        l_depth = Solution.maxDepth(self, root.left)
        r_depth = Solution.maxDepth(self, root.right)

        return max(l_depth, r_depth) + 1


s = Solution()

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(s.maxDepth(root))

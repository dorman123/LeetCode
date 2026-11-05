from typing import Optional, List

class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

class Solution:
    def preorderTraversal(self, root: Optional[Node]) -> List[int]:
        if root is None:
            return []

        # שורש → שמאל → ימין
        result = [root.data]
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result

if __name__ == "__main__":
    # Build the tree
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    s = Solution()
    output = s.preorderTraversal(root)
    print("Preorder Traversal:", output)

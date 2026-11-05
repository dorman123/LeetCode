# Python3 code to implement the approach

# Class describing a node of the tree
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

class Solution:
    # Inorder Traversal
    @classmethod
    def inorderTraversal(cls, root):
        if root:
            # Traverse left subtree
            Solution.inorderTraversal(root.left)

            # Visit node
            print(root.data, end=" ")

            # Traverse right subtree
            Solution.inorderTraversal(root.right)

s = Solution()

if __name__ == "__main__":
    # Build the tree
    root = Node(10)
    root.left = Node(25)
    root.right = Node(30)
    root.left.left = Node(20)
    root.left.right = Node(35)
    root.right.left = Node(15)
    root.right.right = Node(45)

    # Function call
    print("Inorder Traversal:", end=" ")
    s.inorderTraversal(root)

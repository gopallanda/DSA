class Node:
    def __init__(self,data):
        self.left=None 
        self.right=None 
        self.data=data 
        #       5
        #     / \   
        #   12   13
        #   /  \    \
        #  7    14   2
        # /  \ /  \  / \
        #17 23 27  3 8  11 
def inOrder_traversal(root):
    if root is  None:
        return 
    inOrder_traversal(root.left)
    print(root.data,end="->")
    
    inOrder_traversal(root.right)
def PreOrder_traversal(root):
    if root is None:
        return 
    print(root.data,end="->")
    PreOrder_traversal(root.left)
    PreOrder_traversal(root.right)
def PostOrder_traversal(root):
    if root is None:
        return 
    PostOrder_traversal(root.left)
    PostOrder_traversal(root.right)
    print(root.data,end="->") 
if __name__=="__main__":
    root=Node(5)
    root.left=Node(12)
    root.right=Node(13)
    root.left.left=Node(7)
    root.left.right=Node(14)
    root.right.right=Node(2)
    root.left.left.left=Node(17)
    root.left.left.right=Node(23)
    root.left.right.left=Node(27)
    root.left.right.right=Node(3)
    root.right.right.left=Node(8)
    root.right.right.right=Node(11)
    print("InOrder Traversal:")
    inOrder_traversal(root)
    print("\nPreOrder Traversal:")
    PreOrder_traversal(root)
    print("\nPostOrder Traversal:")
    PostOrder_traversal(root)
    
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None  

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.val:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def dfs(self, root):
        def preorder(root):
            if root is None:
                return  
            print(root.val)  
            preorder(root.left)  
            preorder(root.right)
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            print(root.val)
            inorder(root.right)
        def postorder(root):
            if root is None:
                return
            inorder(root.left)
            inorder(root.right)
            print(root.val)
        print(f"preoder is :- {preorder(root)}")
        print(f"inorder is :- {inorder(root)}")
        print(f"postorder is :- {postorder(root)}")

if __name__ == "__main__":
    bst = BSTree()  
    bst.root = bst.insert(bst.root, 3)  
    bst.insert(bst.root, 4)  
    bst.insert(bst.root, 2)
    bst.dfs(bst.root)

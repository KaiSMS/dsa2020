class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.right = buildTree(inorder[mid+1:], postorder)
    root.left = buildTree(inorder[:mid], postorder)
    return root

def printTree(root, depth):
    if not root:
        return
    print('\t' * depth + root.val)
    if not root.left and root.right:
        print('\t' * (depth + 1) + '*')
    printTree(root.left, depth + 1)
    printTree(root.right, depth + 1)

# 读取输入
inorder = input().strip()
postorder = input().strip()

# 重建二叉树
tree = buildTree(list(inorder), list(postorder))

# 输出文本缩进二叉树
printTree(tree, 0)
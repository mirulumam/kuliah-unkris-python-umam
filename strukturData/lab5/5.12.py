from myBinaryTree import buildParseTree

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(preorder(pt))

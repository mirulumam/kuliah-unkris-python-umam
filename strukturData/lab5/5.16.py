from myBinaryTree import buildParseTree


def inorder(tree):
    if tree!=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())   
    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(inorder(pt))

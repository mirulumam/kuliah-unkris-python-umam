from myBinaryTree import buildParseTree


def postorder(tree):
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
postorder(pt)

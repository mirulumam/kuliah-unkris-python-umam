from myBinaryTree import buildParseTree


def printexp(tree):
    sVal=""
    if tree:
        sVal='('+printexp(tree.getLeftChild())
        sVal=sVal+str(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+')'
    return sVal 
    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(printexp(pt))

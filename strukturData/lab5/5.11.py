import operator

from myBinaryTree import buildParseTree

def evaluate(parseTree):
    opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    if parseTree.getLeftChild() and parseTree.getRightChild():
        fn=opers[parseTree.getRootVal()]
        return fn(evaluate(parseTree.getLeftChild()),evaluate(parseTree.getRightChild()))
    else: return parseTree.getRootVal()
    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))

from myBinaryTree import buildParseTree

def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

    
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(preorder(pt))



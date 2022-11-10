class BinaryTree:
    
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def getRightChild(self):
		return self.rightChild
	def getLeftChild(self):
		return self.leftChild
	def setRootVal(self, obj):
		self.key = obj
	def getRootVal(self):
		return self.key

r = BinaryTree('A')
print(r.getRootVal())


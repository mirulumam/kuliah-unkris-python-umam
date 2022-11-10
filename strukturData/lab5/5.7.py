class BinaryTree:
    
	def __init__(self,rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t


	def getRightChild(self):
		return self.rightChild
	def getLeftChild(self):
		return self.leftChild
	def setRootVal(self,obj):
		self.key = obj
	def getRootVal(self):
		return self.key

r = BinaryTree('A')
r.insertRight('C')
print(r.getRightChild())
print(r.getRightChild().getRootVal())

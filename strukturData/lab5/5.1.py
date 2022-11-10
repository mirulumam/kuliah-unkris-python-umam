def BinaryTree(r):
    return [r, [], []]


def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

print("BinaryTree 1")
r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
print(r)

print("\nBinaryTree 2")
s = BinaryTree(10)
insertLeft(s, 20)
insertLeft(s, 30)
print(s)

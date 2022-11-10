def BinaryTree(r):
    return [r, [], []]


def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch,[],t])
    else:
        root.insert(2, [newBranch,[],[]])
    return root

print("BinaryTree 1")
r = BinaryTree(3)
insertRight(r, 6)
insertRight(r, 7)
print(r)

print("\nBinaryTree 2")
s = BinaryTree(15)
insertRight(s, 25)
insertRight(s, 35)
print(s)
def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint = len(alist) // 2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist[ : midpoint], item)
			else:
				return binarySearch(alist[midpoint+1 : ], item)

print("Test 1")
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

print("\nTest 2")
testlist2 = [7, 42, 25, 20, 24, 23, 34, 43, 50]
print(binarySearch(testlist2, 11))
print(binarySearch(testlist2, 24))
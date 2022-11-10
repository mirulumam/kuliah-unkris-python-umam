def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False
	while first <= last and not found:
		midpoint = (first + last)//2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
		return found

print("Test 1")
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

print("\nTest 2")
testlist2 = [7, 42, 25, 20, 24, 23, 34, 43, 50]
print(binarySearch(testlist2, 11))
print(binarySearch(testlist2, 24))

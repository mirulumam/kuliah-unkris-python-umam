def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False
	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos = pos+1
	return found

print("Test 1")
testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(orderedSequentialSearch(testlist1, 3))
print(orderedSequentialSearch(testlist1, 13))

print("\nTest 2")
testlist2 = [7, 42, 25, 20, 24, 23, 34, 43, 50]
print(orderedSequentialSearch(testlist2, 11))
print(orderedSequentialSearch(testlist2, 24))
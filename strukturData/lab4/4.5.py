def sequentialSearch(alist, item):
	pos = 0
	found = False
	while pos < len(alist) and not found:
		if alist[pos] == item: found = True
		else: pos = pos+1
	return found

print("Test 1")
testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist1, 3))
print(sequentialSearch(testlist1, 13))

print("\nTest 2")
testlist2 = [7, 42, 25, 20, 24, 23, 34, 43, 50]
print(sequentialSearch(testlist2, 11))
print(sequentialSearch(testlist2, 24))
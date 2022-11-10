def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

print("Bubble Sort 1")
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)

print("\nBubble Sort 2")
alist2 = [72, 87, 95, 62, 65, 46, 76, 44, 97]
bubbleSort(alist2)
print(alist2)
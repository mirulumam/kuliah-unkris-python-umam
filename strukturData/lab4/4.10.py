def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passnum = passnum-1

print("Short Bubble Sort 1")
alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)

print("\nShort Bubble Sort 2")
alist2 = [25, 35, 45, 95, 55, 65, 75, 85, 105, 115]
shortBubbleSort(alist2)
print(alist2)

i = 1
L1 = []
L = []
n = int(input("MASUK BANYAKNYA LIST : "))
while i <=n:
    print("MASUKAN NIM : ", i, ":", end=" ")
    nim = int(input(""))
    print("MASUKAN NAMA : ", i, ":", end=" ")
    nama = input("")
    i = i + 1
    L1 = [nim, nama]
    L.append(L1)

print()
print(L)
print()

#searching

find = int(input("input nim yang dicari : "))
a = 0
b = len(L)-1
sucess = False
L.sort()
while a<=b and not sucess:
    mid = (a+b)//2
    for i in L:
        if L[mid][0]==find:
            hasil = L[mid][1]
            sucess = True
        else:
            if find<L[mid][0]:
                a = mid+1
if sucess:
    print("nama mahasiswa : ", hasil)
else :
    print("tidak di temukan")

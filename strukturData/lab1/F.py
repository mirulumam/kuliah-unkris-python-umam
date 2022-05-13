# thanks to: https://stackoverflow.com/q/29155829

def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

class F:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
        # 1.10 Tugas Lanjutan (4)
        if not isinstance(top, int) or not isinstance(bottom, int):
            raise ValueError("Pembilang dan/atau Penyebut harus integer")
        
        # 1.11 Tugas Mandiri (5)
        if top < 0 or bottom < 0:
            raise ValueError("Pembilang dan/atau Penyebut harus lebih dari 0")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self, o):
        newnum = self.num * o.den + self.den * o.num
        newden = self.den * o.den
        common = gcd(newnum, newden)
        return F(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    # 1.9 Tugas Pendahuluan (1)
    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den
        
    # 1.10 Tugas Lanjutan (2)
    def __sub__(self, o):
        newnum = self.num * o.den - self.den * o.num
        newden = self.den * o.den
        return F(newnum, newden)

    def __mul__ (self, o):
        newnum = self.num * o.num
        newden = self.den * o.den
        return F(newnum, newden)

    def __truediv__(self, o):
        newnum = self.num * o.den
        newden = self.den * o.num
        return F(newnum, newden)
        
    # 1.10 Tugas Lanjutan (3)
    def __gt__(self, o):
        return self.num/self.den > o.num/o.den
    
    def __ge__(self, o):
        return self.num/self.den >= o.num/o.den
    
    def __lt__(self, o):
        return (self.num * self.den) < (o.num * o.den)
    
    def __ne__(self, o):
        return (self.num * self.den) != (o.num * o.den)
        
    # 1.11 Tugas Mandiri (6)
    # thanks to: https://stackoverflow.com/a/22260266
    def __radd__(self, o):
        return self.__add__(o)
    # perbedaan __radd__ dan __add__ adalah
    # pada penempatan object di operasi aritmatika
    # jika object (self) ada di sebelah kanan, __radd__ yang akan dipanggil
    # selain itu, __add__ yang akan dipanggil
    
    # 1.11 Tugas Mandiri (7)
    # thanks to: https://teamtreehouse.com/community/what-is-the-purpose-of-the-iadd-magic-method-since-it-works-fine-without-it
    def __iadd__(self, o):
        self = self.__add__(o)
        return self
    # _iadd_ menyimpan hasil penjumlahan menggunakan operasi +=
    # sementara __add__ tidak. __add_ membutuhkan variabel atau object lain
    # untuk menyimpan hasil penjumlahannya
    # contoh add() dan iadd() sebelum override:
    # __add__               __iadd__
    # a = F(1, 2)           a = F(1, 2)
    # b = F(2, 4)           b = F(2, 4)
    # a + b                 a += b
    # prin(a) -> 1/2        print(a) -> 1/1
    # c = a + b
    # print(c) -> 1/1
    
    # 1.11 Tugas Mandiri (8)
    def __repr__(self):
        return str(self)
    # repr() menampilkan object secara unambiguous
    # artinya, object akan ditampilkan apa adanya
    # sedangkan str() menampilkan object agar lebih manusiawi
    # contoh str dan repr sebelum override:
    # str()             repr()
    # a = F(1, 2)       a = F(1, 2)
    # str(a) -> 1/2     repr(a) -> <__main__.F object at 0x7f753c6fad90>

    def tugasPendahuluan(self):
        print("numerator \t", self.getNum())
        print("denominator \t", self.getDen())

    def tugasLanjutan2(self, other):
        print("a - b \t\t", (self-other))
        print("a * b \t\t", (self*other))
        print("a / b \t\t", (self/other))

    def tugasLanjutan3(self, o):
        print("a > b \t", (self>o))
        print("a >= b \t", (self>=o))
        print("a < b \t", (self<o))
        print("a <= b \t", (self<=o))
        print("a != b \t", (self!=o))
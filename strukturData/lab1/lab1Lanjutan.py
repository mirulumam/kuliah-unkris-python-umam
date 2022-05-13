from strukturData.lab1.F import F


def lab1TugasLanjutan2():
    f = F(1, 2)
    print("__sub__: a - b \t\t", (f - F(1, 3)))
    print("__mul__: a * b \t\t", (f * F(2, 3)))
    print("__truediv__: a / b \t\t", (f / F(1, 4)))

def lab1TugasLanjutan3():
    f = F(1, 2)
    print("__gt__: a > b \t", (f > F(1, 3)))
    print("__ge__: a >= b \t", (f >= F(1, 3)))
    print("__lt__: a < b \t", (f < F(2, 4)))
    print("__le__: a <= b \t", (f <= F(2, 4)))
    print("__ne__: a != b \t", (f != F(2, 3)))

def lab1TugasLanjutan4():
    print("pembilang dan penyebut berupa integer:")
    try:
        c = F(1, 2)
        print("C\t\t", c.getNum(), "/", c.getDen())
    except ValueError as e:
        print("ERROR", e.args[0])

    print("pembilang atau penyebut bukan integer:")
    try:
        c = F("1", 2)
        print("C\t\t", c.getNum(), "/", c.getDen())
    except ValueError as e:
        print("ERROR", e.args[0])

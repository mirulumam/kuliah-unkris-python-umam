from strukturData.lab2.lab2Tasks import Lab2Task


def lab2Pendahuluan1():
    p = Lab2Task()
    p.testEqual(p.revString1('apple'), 'alppe')
    p.testEqual(p.revString1('x'), 'X')
    p.testEqual(p.revString1('1234567890'), '0987654321')
    print("\n")
    p.testEqual(p.revString2('apple'), 'elppa')
    p.testEqual(p.revString2('x'), 'x')
    p.testEqual(p.revString2('1234567890'), '0978654321')
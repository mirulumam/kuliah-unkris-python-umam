class Pendahuluan:
    # source: https://stackoverflow.com/a/38971811

    # from pythonds.basic.stack import Stack

    # 2.5 Tugas Pendahuluan (1)
    def revString1(string):
        return string[::-1]

    def revString2(string):
        # s = Stack() # this is how i have myStack
        s = []

        for ch in string:
            s.append(ch) # push the characters to form a stack

        result = '' # form an empty reverse string
        while len(s):
            # adding my characters to the empty reverse string in reverse order
            result = result + s.pop()

        return result

    def testEqual(s1, s2):
        print("VALID ?", s1 == s2)

    def result():
        testEqual(revString1('apple'), 'alppe')
        testEqual(revString1('x'), 'X')
        testEqual(revString1('1234567890'), '0987654321')
        print("\n")
        testEqual(revString2('apple'), 'elppa')
        testEqual(revString2('x'), 'x')
        testEqual(revString2('1234567890'), '0978654321')
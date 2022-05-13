import re
from .infixPostfix import infixToPostfix, postFixEvaluation, infixEvaluation
from .queue import Queue, doQueue, doDequeue

class Lab2Task:

    # source: https://stackoverflow.com/a/38971811

    # from pythonds.basic.stack import Stack

    # 2.5 Tugas Pendahuluan (1)
    def revString1(self, string):
        return string[::-1]

    def revString2(self, string):
        # s = Stack() # this is how i have myStack
        s = []

        for ch in string:
            s.append(ch) # push the characters to form a stack

        result = '' # form an empty reverse string
        while len(s):
            # adding my characters to the empty reverse string in reverse order
            result = result + s.pop()

        return result

    def testEqual(self, s1, s2):
        print("VALID ?", s1 == s2)

    # 2.6 Tugas Lanjutan (2)
    def reverseList(self, list):
        list.reverse()
        print(list)

    # 2.6 Tugas Lanjutan (3)
    # thanks to: https://stackoverflow.com/a/11230103
    def htmlTagFinder(self):
        html = "<html><head><title>Contoh Halaman Web</title></head><body><h1>Halo kawan, Saya belajar Python dan HTML</h1></body></html>"
        result = re.findall("<[^>]*>", html)
        print(result)

    # 2.6 Tugas Lanjutan (4)
    def infixToPostfixResult(self):
        print(infixToPostfix("A * B + C * D"))
        print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
        print(infixToPostfix("(2+3)^4-((5+6)-(7*8))"))

    # 2.6 Tugas Mandiri (5)
    def postFixEvaluationResult(self):
        print(postFixEvaluation("7 8 + 3 2 + /"))

    # 2.6 Tugas Mandiri (6 dan 7)
    def evaluatorDirectInfix(self):
        infix = "(2+3)^4-((5+6)-(7*8))"
        print("Infix", infix)
        inToPost = infixToPostfix(infix)
        print("Infix to Postfix", inToPost)
        evaluation = infixEvaluation(inToPost)
        print("Evaluation", evaluation)

    # 2.6 Tugas Mandiri (8)
    def queueDequeue(self):
        q = doQueue(Queue(), 10000)
        d = doDequeue(q)
        if q.getTime() < d.getTime():
            o1 = "Queue"
            s = "lebih cepat"
            o2 = "Dequeue"
        else:
            o1 = "Dequeue"
            s = "lebih cepat"
            o2 = "Queue"
        print("Kseimpulan: {0} {1} daripada {2}".format(o1, s, o2))
        

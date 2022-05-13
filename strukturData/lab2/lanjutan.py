import re
from .infixPostfix import evaluation, infixToPostfix, postFixEvaluation, infixEvaluation
from .queue import Queue, doQueue, doDequeue

class Lanjutan:

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

    # 2.6 Tugas Lanjutan (5)
    def postFixEvaluationResult(self):
        print(postFixEvaluation("7 8 + 3 2 + /"))

    # 2.6 Tugas Lanjutan (6 dan 7)
    def evaluatorDirectInfix(self):
        infix = "(2+3)^4-((5+6)-(7*8))"
        print("Infix", infix)
        inToPost = infixToPostfix(infix)
        print("Infix to Postfix", inToPost)
        evaluation = infixEvaluation(inToPost)
        print("Evaluation", evaluation)

    # 2.6 Tugas Lanjutan (8)
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
        

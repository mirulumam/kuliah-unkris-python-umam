import re
from infixToPostfix import infixToPostfix

class Lanjutan:

    # 2.6 Tugas Lanjutan (2)
    def reverseList(list):
        list.reverse()
        print(list)

    # 2.6 Tugas Lanjutan (3)
    # thanks to: https://stackoverflow.com/a/11230103
    def htmlTagFinder():
        html = "<html><head><title>Contoh Halaman Web</title></head><body><h1>Halo kawan, Saya belajar Python dan HTML</h1></body></html>"
        result = re.findall("<[^>]*>", html)
        print(result)

    # 2.6 Tugas Lanjutan (4)
    def infixToPostfixResult():
        print(infixToPostfix("A * B + C * D"))
        print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


from strukturData.lab1.F import F
from helper import cls
from strukturData.lab1.sudoku import showSudokuResult
from strukturData.lab2.infixToPostfix import infixToPostfix

cls()

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("(A+B)^C-((D+E)-(B*F))"))

# a = F(2, 5)
# b = F(1, 5)
# print("A: ", a.getNum(), "/", a.getDen(), "\tB: ", b.getNum(), "/", b.getDen())

# print("\nLab 1 - Tugas Pendahuluan - 1")
# a.tugasPendahuluan()

# print("\nLab 1 - Tugas Lanjutan - 2")
# a.tugasLanjutan2(b)

# print("Lab 1 - Tugas Lanjutan - 3")
# a.tugasLanjutan3(b)
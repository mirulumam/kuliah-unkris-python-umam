from strukturData.lab1.F import F
from strukturData.lab1.card.cardGame import Game
from strukturData.lab1.sudoku import showSudokuResult


def tugasMandiri5():
    print("pembilang dan penyebut berupa angka positif:")
    try:
        c = F(1, 2)
        print("C\t\t", c.getNum(), "/", c.getDen())
    except ValueError as e:
        print("ERROR", e.args[0])

    print("pembilang dan penyebut berupa angka negatif:")
    try:
        c = F(-1, 2)
        print("C\t\t", c.getNum(), "/", c.getDen())
    except ValueError as e:
        print("ERROR", e.args[0])

def tugasMandiri6():
    a = F(1, 2)
    b = F(2, 4)
    c = a + b
    print("__radd__", c.getNum(), "/", c.getDen())

def tugasMandiri7():
    a = F(1, 2)
    b = F(2, 4)
    c = F(3, 4)
    a + b
    print("__add__", a.getNum(), "/", a.getDen())
    a += b
    print("__iadd__", a.getNum(), "/", a.getDen())
    a + c
    print("__add__", a.getNum(), "/", a.getDen())

def tugasMandiri8():
    a = F(1, 2)
    print(a.__repr__())

def tugasMandiri9():
    g = Game("Ganyu", "Shenhe")
    g.play_game()

def tugasMandiri10():
    showSudokuResult()

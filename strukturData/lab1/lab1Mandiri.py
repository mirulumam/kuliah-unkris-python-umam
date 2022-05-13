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

def tugasMandiri9():
    g = Game("Ganyu", "Shenhe")
    g.play_game()

def tugasMandiri10():
    showSudokuResult()

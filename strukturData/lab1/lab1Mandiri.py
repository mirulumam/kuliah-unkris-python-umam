from strukturData.lab1.F import F


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


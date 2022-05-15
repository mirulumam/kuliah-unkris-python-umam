from .antColony import AntColony

def antColonyTask():
    print("Please wait...")
    # given some nodes, and some locations...
    test_nodes = {
        0: (3, 6),
        1: (8, 9),
        2: (2, 4, 6, 9),
        3: (7, 8, 9),
        4: (1, 1, 2, 7),
        5: (2, 4),
        6: (1, 3, 5),
        7: (1, 3, 9),
        8: (3, 5, 2)
    }

    # ...and a function to get distance between nodes...
    def distance(start, end):
        x_distance = abs(start[0] - end[0])
        y_distance = abs(start[1] - end[1])
        
        # c = sqrt(a^2 + b^2)
        import math
        return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

    # ...we can make a colony of ants...
    colony = AntColony(test_nodes, distance)

    # ...that will find the optimal solution with ACO
    print(colony.mainloop())
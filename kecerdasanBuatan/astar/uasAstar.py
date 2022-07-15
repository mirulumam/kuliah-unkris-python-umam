import astar

nodes = {
        'S' : [ ('C', 5), ('A', 2) ],
        'A' : [ ('B', 4), ('D', 2) ],
        'B' : [ ('G', 2) ],
        'C' : [ ('B', 2), ('G', 3) ],
        'D' : [ ('B', 2), ('G', 4) ]
         }

costs = { 'S' : 3, 'A' : 3, 'B' : 6, 'C' : 3, 'D' : 6, 'G' : 4 }


def neighbors(n):
    for n1, d in nodes[n]: yield n1

def distance(n1, n2):
    for n, d in nodes[n1]:
        if n == n2: return d

def cost(n,goal):
    costn = costs.get(n)
    return costn

#target (asal, tujuan)
path = list(astar.find_path(
    'S', 'G',
    neighbors_fnct=neighbors,
    heuristic_cost_estimate_fnct=cost,
    distance_between_fnct=distance
    ))

print("Jalur Terpendek:", path)
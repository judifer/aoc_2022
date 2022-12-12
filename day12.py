import networkx as nx

data = [[(ord(x)- 96) for x in y.strip()] for y in open("day12.txt")]

def generate_graph(data):
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data[0])):
            G.add_node((x, y))
            neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for nex, ney in neighbours:
                if 0 <= nex < len(data[0]) and 0 <= ney < len(data):
                    if data[ney][nex] - data[y][x] <= 1:
                        G.add_edge((x, y), (nex, ney), weight=data[ney][nex])
    return G

def calc_paths(sourcey, goal, graph):
    G = graph
    path = nx.shortest_path(G, source=sourcey, target=goal)
    risk = sum(data[y][x] for x, y in path[1:])
    return len(path) - 1

for y, i in enumerate(data):
    for x, j in enumerate(i):
        if j == (ord("S") - 96):
            data[y][x] = 0
            sourcey = (x, y)
        elif j == (ord("E")- 96):
            data[y][x] = 26
            goal = (x, y)
graph = generate_graph(data)
first_path = calc_paths(sourcey, goal, graph)

paths = list()
paths.append(first_path)

for y, i in enumerate(data):
    for x, j in enumerate(i):
        if j == (ord("a") - 96):
            sourcey = (x, y)
            try:
                paths.append(calc_paths(sourcey, goal, graph))
            except:
                pass

print(f"Part one: {first_path} | Part two: {min(paths)}")
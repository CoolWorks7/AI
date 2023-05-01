graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": [],
    "D": ["G"],
    "E": [],
    "F": ["H", "I"],
    "G": ["J", "K"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
}


def breadth_first_search(goal):
    closed = []
    open = [list(graph)[0]]

    while open is not []:
        X = open[0]
        open.pop(0)
        if X == goal:
            closed.append(X)
            return closed
        else:
            closed.append(X)
            for i in range(len(graph[X])):
                if graph[X][i] in open or graph[X][i] in closed:
                    pass
                else:
                    open.append(graph[X][i])
    return "Not Found!"


def depth_first_search(goal):
    closed = []
    open = [list(graph)[0]]

    while open is not []:
        X = open[0]
        open.pop(0)
        if X == goal:
            closed.append(X)
            return closed
        else:
            closed.append(X)
            for i in reversed(range(len(graph[X]))):
                if graph[X][i] in open or graph[X][i] in closed:
                    pass
                else:
                    open.insert(0, graph[X][i])
    return "Not Found!"


print(breadth_first_search("G"))
print(depth_first_search("G"))

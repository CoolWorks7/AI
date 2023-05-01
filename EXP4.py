def aStartSearch(start, goal):
    opened = set(start)
    closed = set()
    g = {}
    parent = {}

    g[start] = 0
    parent[start] = start

    while len(opened) > 0:
        n = None

        for v in opened:
            if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == goal or graph[n] == []:
            pass
        else:
            child = graph[n]
            for i in range(len(child)):
                m = child[i]["node"]
                dist = child[i]["dist"]

                if m not in opened and m not in closed:
                    opened.add(m)
                    parent[m] = n
                    g[m] = g[n] + dist
                else:
                    if g[m] > g[n] + dist:
                        g[m] = g[n] + dist
                        parent[m] = n

                        if m in closed:
                            closed.remove(m)
                            opened.add(m)
        if n is None:
            return None

        if n == goal:
            costVal = g[n]
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start)
            path.reverse()

            return path, costVal

        opened.remove(n)
        closed.add(n)

    return None, None


graph = {
    "A": [{"node": "B", "dist": 4}, {"node": "C", "dist": 3}],
    "B": [{"node": "F", "dist": 5}, {"node": "D", "dist": 8}],
    "C": [{"node": "D", "dist": 10}, {"node": "E", "dist": 7}],
    "D": [{"node": "G", "dist": 5}],
    "E": [{"node": "D", "dist": 2}],
    "F": [{"node": "G", "dist": 16}],
    "G": []
}

heuristic = {
    "A": 14,
    "B": 12,
    "C": 11,
    "D": 6,
    "E": 4,
    "F": 11,
    "G": 0,
}

s = 'A'
g = 'D'
path, cost = aStartSearch(s, g)

print('\n\tStart Node: ' + s)
print('\tGoal Node: ' + g)

if path and cost:
    track = ""
    for i in range(len(path)):
        if i == len(path) - 1:
            track += str(path[i])
        else:
            track += str(path[i]) + ' --> '
    print('\n\tpath found: {}'.format(track))
    print('\tCost: {}'.format(cost))

else:
    print('Path does not exists')

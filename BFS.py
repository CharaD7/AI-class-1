graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs_paths(graph, start, goal):
    paths = []
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path): #delete previous expanded (path)
            if next == goal:
                paths.append(path + [next])
            else:
                queue.append((next, path + [next]))
    return paths

print bfs_paths(graph, 'A', 'F')
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

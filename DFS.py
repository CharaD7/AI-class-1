graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal):
    paths = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                paths.append(path + [next])
            else:
                stack.append((next, path + [next]))
    return paths

print dfs_paths(graph, 'A', 'F')
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

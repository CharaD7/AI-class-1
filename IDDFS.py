graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_paths(graph, start, goal, limit):
    paths = []
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        depth = len(path)        
        for next in graph[vertex] - set(path):
            if next == goal:
                paths.append(path + [next])
            else:
                if(depth+1<=limit):        
                    stack.append((next, path + [next]))
    return paths

def IDDFS(graph, start, goal):
    for i in range(1, 4+1):
        paths=dfs_paths(graph, start, goal, limit=i)
        if(paths):
            print paths

IDDFS(graph, 'A', 'F')
## [['A', 'C', 'F']]
## [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
## [['A', 'B', 'E', 'F'], ['A', 'C', 'F']]
##print dfs_paths(graph, 'A', 'F', 1)

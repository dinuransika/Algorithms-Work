from collections import defaultdict
import queue
class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
    
    def connect(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def find_all_distances(self, s):
        unvisted = set([i for i in range(self.n)])
        q = queue.Queue()
        distances = [-1 for _ in range(self.n)]
        distances[s] = 0
        unvisted.remove(s)
        q.put(s)
        while not q.empty():
            node = q.get()
            children = self.graph[node]
            height = distances[node]
            for child in children:
                if child in unvisted:
                    distances[child] = height + 6
                    unvisted.remove(child)
                    q.put(child)
        distances.pop(s)
        print(" ".join(map(str, distances)))

g = Graph(4)
g.connect(0, 1)
g.connect(0, 2)
print(g.graph)
g.find_all_distances(0)
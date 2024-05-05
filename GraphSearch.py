class AdjacencyMatrix:
    def __init__(self):
        self.graph = []
        self.vertices = {}

    '''readGraph(filepath) reads the text file given at filepath
    and initializes a graph based on the information in the file and returns
    True if it is able to successfully read and create a graph, False
    otherwise (you may choose to print. '''

    def readGraph(self, filepath):
        try:
            with open(filepath, 'r') as file:
                num_vertices, num_edges = map(int, file.readline().split())
                vertices = file.readline().strip().split(',')
                self.vertices = {vertex: index for index, vertex in enumerate(vertices)}
                self.graph = [[0] * num_vertices for _ in range(num_vertices)]
                for _ in range(num_edges):
                    v1, v2 = file.readline().split()
                    self.addEdge((v1, v2))
            return True
        except Exception as e:
            print(f"Error reading graph from {filepath}: {e}")
            return False
        
    '''addVertex(vertex) adds a vertex to the graph indicated by the
    vertex string. If the vertex already exists, do nothing. This method
    returns True on success, False otherwise.'''

    def addVertex(self, vertex):
        if vertex not in self.vertices:
            index = len(self.vertices)
            self.vertices[vertex] = index
            for row in self.graph:
                row.append(0)
            self.graph.append([0] * (index + 1))
            return True
        return False
    
    '''addEdge(edge) adds an edge represented by the 2-tuple edge to
    the graph. If the edge already exists, do nothing. The method should
    ensure that the vertices in the edge already exist in the vertex and
    should return False if either is not present. On successful addition,
    the method should return True.'''

    def addEdge(self, edge):
        v1, v2 = edge
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        index1, index2 = self.vertices[v1], self.vertices[v2]
        if self.graph[index1][index2] == 0:
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1
            return True
        return False
    
    '''deleteVertex(vertex) deletes a vertex from the graph
    indicated by vertex. Note that deletion on a vertex should include
    deletion of all edges associated with the vertex. On successful
    deletion, the method returns True, False otherwise.'''

    def deleteVertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices[vertex]
            del self.vertices[vertex]
            del self.graph[index]
            for row in self.graph:
                del row[index]
            return True
        return False
    
    '''deleteEdge(edge) deletes the edge indicated by the 2-tuple
    edge. If the edge does not exist, return False. If the edge is
    successfully deleted, return True.'''

    def deleteEdge(self, edge):
        v1, v2 = edge
        if v1 not in self.vertices or v2 not in self.vertices:
            return False
        index1, index2 = self.vertices[v1], self.vertices[v2]
        if self.graph[index1][index2] == 1:
            self.graph[index1][index2] = 0
            self.graph[index2][index1] = 0
            return True
        return False
    
    '''getNeighbors(vertex) returns the neighbors (vertices
    associated with the given vertex with an edge) as a list. If the vertex
    has no neighbors, return an empty list. If the vertex does not exist,
    return False.'''

    def getNeighbors(self, vertex):
        if vertex in self.vertices:
            index = self.vertices[vertex]
            neighbors = []
            for i, val in enumerate(self.graph[index]):
                if val == 1:
                    neighbors.append(list(self.vertices.keys())[i])
            return neighbors
        return False


class AdjacencyList:
    def __init__(self):
        self.graph = {}
    
    def readGraph(self, filepath):
        try:
            with open(filepath, 'r') as file:
                num_vertices, num_edges = map(int, file.readline().split())
                vertices = file.readline().strip().split(',')
                self.graph = {vertex: [] for vertex in vertices}
                for _ in range(num_edges):
                    v1, v2 = file.readline().split()
                    self.addEdge((v1, v2))
            return True
        except Exception as e:
            print(f"Error reading graph from {filepath}: {e}")
            return False

    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        return False

    def addEdge(self, edge):
        v1, v2 = edge
        if v1 not in self.graph or v2 not in self.graph:
            return False
        if v2 not in self.graph[v1]:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            return True
        return False

    def deleteVertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
            return True
        return False

    def deleteEdge(self, edge):
        v1, v2 = edge
        if v1 in self.graph and v2 in self.graph:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
                return True
        return False

    def getNeighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return False


'''Implement a function BFS(graph, start_vertex, end_vertex)
that implements Breadth-First Search on the given
graph(AdjacencyMatrix or AdjacencyList), starting at
start_vertex and ending at end_vertex. The function should return
a list of edge tuples indicating the path from start_vertex to
end_vertex, should one exist. If a path does not exist, return an empty
list. If either vertex does not exist in the graph, return False. In comments,
describe the average running time for BFS on a graph 𝐺 = {𝑉, 𝐸} where V
and E are sets of vertices and edges.'''

from collections import deque

def BFS(graph, start_vertex, end_vertex):
    if start_vertex not in graph.vertices or end_vertex not in graph.vertices:
        return []

    queue = deque([(start_vertex, [])])
    visited = set()

    while queue:
        current_vertex, path = queue.popleft()
        visited.add(current_vertex)

        if current_vertex == end_vertex:
            return path

        neighbors = graph.getNeighbors(current_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [(current_vertex, neighbor)]))
                visited.add(neighbor)

    return []

'''Average running time for BFS on a graph G = {V, E}:
The worst-case scenario time complexity of O(V + E).
 '''

'''Implement a function DFS(graph, start_vertex, end_vertex)
that implements Depth-First Search on the given graph, starting at
start_vertex and ending at end_vertex. The function should return
a list of edge tuples indicating the path from start_vertex to
end_vertex, should one exist. If a path does not exist, return an empty
list. If either vertex does not exist in the graph, return False. In comments,
describe the average running time for DFS on a graph 𝐺 = {𝑉, 𝐸} where V
and E are sets of vertices and edges.'''

def DFS(graph, start_vertex, end_vertex):
    if start_vertex not in graph.vertices or end_vertex not in graph.vertices:
        return []
    
    visited = set()
    path = []

    def dfs_recursive(current_vertex):
        visited.add(current_vertex)

        if current_vertex == end_vertex:
            return True

        for neighbor in graph.getNeighbors(current_vertex):
            if neighbor not in visited:
                path.append((current_vertex, neighbor))
                if dfs_recursive(neighbor):
                    return True
                path.pop()

        return False

    if dfs_recursive(start_vertex):
        return path
    else:
        return []


'''
Average running time for DFS on a graph G = {V, E}:
In the worst-case scenario, DFS has a time complexity of O(V + E).
'''

'''Using the sample graph.txt file, run the following searches using your
DFS and BFS code. In comments in your code, provide a list of vertices that
your code visits while conducting the search for each method. If the found
path differ between DFS and BFS, discuss why that occurred.
a. Start Vertex: a, End Vertex: p
b. Start Vertex: n, End Vertex: b
c. Start Vertex: g, End Vertex: q
d. Start Vertex: c, End Vertex: o
e. Start Vertex: o, End Vertex: p'''


adj_matrix_graph = AdjacencyMatrix()
adj_list_graph = AdjacencyList()

adj_matrix_graph.readGraph("graph.txt")
adj_list_graph.readGraph("graph.txt")

searches = [
    ('a', 'p'),
    ('n', 'b'),
    ('g', 'q'),
    ('c', 'o'),
    ('o', 'p')
]

for start_vertex, end_vertex in searches:
    print(f"DFS Path from {start_vertex} to {end_vertex}:")
    dfs_path = DFS(adj_matrix_graph, start_vertex, end_vertex)
    print(dfs_path)
    print("Visited vertices:")
    print([vertex[0] for vertex in dfs_path])
    print()

    print(f"BFS Path from {start_vertex} to {end_vertex}:")
    bfs_path = BFS(adj_matrix_graph, start_vertex, end_vertex)
    print(bfs_path)
    print("Visited vertices:")
    print([vertex[0] for vertex in bfs_path])
    print()

'''
DFS Path from a to p:
[('a', 'c'), ('c', 'i'), ('i', 'f'), ('f', 'b'), ('b', 'g'), ('g', 'p')]
Visited vertices:
['a', 'c', 'i', 'f', 'b', 'g']

BFS Path from a to p:
[('a', 'd'), ('d', 'p')]
Visited vertices:
['a', 'd']

DFS Path from n to b:
[('n', 'h'), ('h', 'e'), ('e', 'd'), ('d', 'a'), ('a', 'c'), ('c', 'i'), ('i', 'f'), ('f', 'b')]
Visited vertices:
['n', 'h', 'e', 'd', 'a', 'c', 'i', 'f']

BFS Path from n to b:
[('n', 'h'), ('h', 'e'), ('e', 'f'), ('f', 'b')]
Visited vertices:
['n', 'h', 'e', 'f']

DFS Path from g to q:
[('g', 'a'), ('a', 'c'), ('c', 'i'), ('i', 'f'), ('f', 'b'), ('b', 's'), ('s', 'd'), ('d', 'e'), ('e', 'h'), ('h', 'n'), ('n', 'l'), ('l', 'q')]
Visited vertices:
['g', 'a', 'c', 'i', 'f', 'b', 's', 'd', 'e', 'h', 'n', 'l']

BFS Path from g to q:
[('g', 'a'), ('a', 'c'), ('c', 'l'), ('l', 'q')]
Visited vertices:
['g', 'a', 'c', 'l']

DFS Path from c to o:
[('c', 'a'), ('a', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'i'), ('i', 'k'), ('k', 'm'), ('m', 'r'), ('r', 'n'), ('n', 'h'), ('h', 'o')]
Visited vertices:
['c', 'a', 'd', 'e', 'f', 'i', 'k', 'm', 'r', 'n', 'h']

BFS Path from c to o:
[('c', 'i'), ('i', 'f'), ('f', 'o')]
Visited vertices:
['c', 'i', 'f']

DFS Path from o to p:
[('o', 'f'), ('f', 'b'), ('b', 'g'), ('g', 'a'), ('a', 'c'), ('c', 'i'), ('i', 'k'), ('k', 'm'), ('m', 'r'), ('r', 'n'), ('n', 'h'), ('h', 'e'), ('e', 'd'), ('d', 'p')]
Visited vertices:
['o', 'f', 'b', 'g', 'a', 'c', 'i', 'k', 'm', 'r', 'n', 'h', 'e', 'd']

BFS Path from o to p:
[('o', 'f'), ('f', 'b'), ('b', 'g'), ('g', 'p')]
Visited vertices:
['o', 'f', 'b', 'g']


The DFS prioritizes traversing as far as possible on each branch before backtracking, BFS goes through the graph level by level.
BFS travels the shortest path when it comes to the number of edges. The difference in exploration priorities lead to different paths by DFS and BFS
In the case of the graph used above, we observed differences in the paths found by DFS and BFS due to the graph's structure and the placement 
of start and end vertices. DFS may find paths that go deep into certain branches of the graph, 
while BFS explores all possible paths of the same length before considering longer paths, leading to potentially different paths being found.
'''
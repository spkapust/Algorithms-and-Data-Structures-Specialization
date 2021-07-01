# python3
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id ^ 1].capacity += flow

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))
    
    def max_flow(self, graph, from_, to):
        flow = 0
        found_t = True
        while(found_t):
            current_layer = [0]
            next_layer = []
            scanned = [False] * graph.size()
            path = {}
            path[0] = -1
            scanned[0] = True
            found_t = False
            while(len(current_layer)):
                n = current_layer.pop()
                ids = graph.get_ids(n)
                for id in ids:
                    e = graph.get_edge(id)
                    if not scanned[e.v] and e.capacity > 0:
                        next_layer.append(e.v)
                        path[e.v] = id
                        scanned[e.v] = True
                        if e.v == to:
                            found_t = True
                            break
                if found_t:
                    min_cap = 200000000
                    id = path[to]
                    while(id != -1):
                        edge = graph.get_edge(id)
                        min_cap = min(edge.capacity, min_cap)
                        id = path[edge.u]
                        #print(edge.u, id)
                    
                    id = path[to]
                    while(id != -1):
                        edge = graph.get_edge(id)
                        graph.add_flow(id, min_cap)
                        id = path[edge.u]
                    
                    flow += min_cap
                    break            
                if not len(current_layer):
                    current_layer, next_layer = next_layer, current_layer
            
        return flow

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.

        #source node 0
        #flight nodes 1-n
        #crew nodes n+1 - n+m
        #sink node n+m+1

        n = len(adj_matrix)
        m = len(adj_matrix[0])
        graph = FlowGraph(n+m+2)
        for i in range(1,n+1):
            graph.add_edge(0, i, 1)
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j]:
                    graph.add_edge(i+1, n+j+1, 1)
        for i in range(n+1,n+m+1):
            graph.add_edge(i, n+m+1, 1)
        
        self.max_flow(graph, 0, n+m+1)
        matching = [-1] * n

        for edge in graph.edges:
            if 0 < edge.u < n+1 and n < edge.v < n+m+1 and edge.capacity == 0:
                matching[edge.u - 1] = edge.v - n - 1
        
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()

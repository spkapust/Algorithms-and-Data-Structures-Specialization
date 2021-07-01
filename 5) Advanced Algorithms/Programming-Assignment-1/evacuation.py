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


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
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


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))

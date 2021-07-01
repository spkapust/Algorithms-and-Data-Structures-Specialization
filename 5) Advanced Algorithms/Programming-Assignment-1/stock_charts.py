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

class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

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
    
    def min_charts(self, stock_data):
             
        n = len(stock_data)
        k = len(stock_data[0])
        graph = FlowGraph(2*n+2) 

        for i in range(1,n+1):
            graph.add_edge(0, i, 1)

        for i, stock1 in enumerate(stock_data):
            for j, stock2 in enumerate(stock_data):
                if i == j:
                    continue
                above = all([x > y for x, y in zip(stock_data[i], stock_data[j])])
                if above:
                    graph.add_edge(i+1, n+j+1, 1)
        
        for i in range(n+1, n+n+1):
            graph.add_edge(i,n+n+1,1)

        return n-self.max_flow(graph, 0, n+n+1)

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()

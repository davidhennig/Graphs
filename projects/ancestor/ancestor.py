
class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in the graph")
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    for vertex in ancestors:
        if vertex[0] not in g.vertices:
            g.add_vertex(vertex[0])
        if vertex[1] not in g.vertices:
            g.add_vertex(vertex[1])
    for vertex in ancestors:
        g.add_edge(vertex[1], vertex[0])

    # print(g.vertices)

    if g.vertices[starting_node] == set():
        return -1

    q = Queue()
    q.enqueue([starting_node])
    longest = []
    
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if len(path) > len(longest):
            longest = path
        if len(path) == len(longest) and path[-1] < longest[-1]:
            longest = path
        for neighbor in g.get_neighbors(v):
            new_path = list(path)
            new_path.append(neighbor)
            q.enqueue(new_path)
            print(q.queue)
    return longest[-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 6)
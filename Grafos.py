class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight=None, directed=False):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1][vertex2] = weight
        if not directed:
            self.graph[vertex2][vertex1] = weight

    def display(self):
        print("República Mexicana representada en un grafo con sus relaciones:")
        for vertex, edges in self.graph.items():
            print(f"El estado {vertex} tiene como conexiones a:")
            for neighbor, weight in edges.items():
                if weight:
                    print(f"  - {neighbor} (costo: {weight})")
                else:
                    print(f"  - {neighbor}")

    def sin_repetir(self, start):
        visited = set()
        path = []
        total_cost = self.sin_repetir_r(start, visited, path)
        print(f"\nRecorrido sin repetir ningún estado (a): {' -> '.join(path)}")
        print(f"Costo total: {total_cost}")
        return total_cost

    def sin_repetir_r(self, vertex, visited, path):
        visited.add(vertex)
        path.append(vertex)
        total_cost = 0
        for neighbor, weight in self.graph[vertex].items():
            if neighbor not in visited:
                total_cost += weight if weight else 0
                total_cost += self.sin_repetir_r(neighbor, visited, path)
        return total_cost

    def repetir(self, start, repeat_vertex):
        visited = set()
        path = []
        total_cost = self.repetir_r(start, visited, path, repeat_vertex)
        print(f"\nRecorrido repitiendo al menos un estado (b): {' -> '.join(path)}")
        print(f"Costo total: {total_cost}")
        return total_cost

    def repetir_r(self, vertex, visited, path, repeat_vertex):
        visited.add(vertex)
        path.append(vertex)
        total_cost = 0
        for neighbor, weight in self.graph[vertex].items():
            if neighbor == repeat_vertex or neighbor not in visited:
                total_cost += weight if weight else 0
                total_cost += self.repetir_r(neighbor, visited, path, repeat_vertex)
        return total_cost


g = Graph()

vertices = ['CDMX', 'Jalisco', 'Nuevo León', 'Puebla', 'Veracruz', 'Chiapas', 'Yucatán']
for vertex in vertices:
    g.add_vertex(vertex)

g.add_edge('CDMX', 'Jalisco', weight=5)
g.add_edge('CDMX', 'Nuevo León', weight=3)
g.add_edge('CDMX', 'Puebla', weight=7)
g.add_edge('Jalisco', 'Veracruz', weight=4)
g.add_edge('Nuevo León', 'Chiapas', weight=6)
g.add_edge('Puebla', 'Yucatán', weight=2)
g.add_edge('Veracruz', 'Chiapas', weight=8)
g.add_edge('Chiapas', 'Yucatán', weight=1)
g.add_edge('Yucatán', 'CDMX', weight=9)

g.display()

g.sin_repetir('CDMX')

g.repetir('CDMX', 'Nuevo León')

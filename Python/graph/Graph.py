from _interfaces import Graph

def main():
    adj = AdjacencyGraph()
    mat = MatrixGraph()

    adj.insert_vertex('A', ['B', 'C', 'D'])
    adj.insert_edge('D', 'B')
    print(adj)
    if 'B' in adj:
        print('B is in adj')
    print(len(adj))
    print(f'num edges = {adj.num_edges()}')

class AdjacencyGraph(Graph):
    def __init__(self):
        """
        Initialization method
        """
        self.__internal_dict = {}
        self.__edges = 0

    def __iter__(self):
        """
        Iterates through the vertices of the Graph
        """
        return iter(self.__internal_dict)

    def __contains__(self, item):
        """
        Sees if a vertice is in the Graph
        """
        return str(item) in self.__internal_dict

    def __eq__(self, other) -> bool:
        """
        Determines if one Graph is the logical equivalent of another
        """
        if issubclass(other, Graph):
            if type(other) == type(self):
                for vertice in self.__internal_dict:
                    if vertice not in other:
                        return False
                    # If either set diff not None
                    other_vertice = other.__internal_dict[vertice]
                    this_vertice = self.__internal_dict[vertice]
                    if other_vertice - this_vertice or this_vertice - other_vertice:
                        return False
                    return True
            elif type(other) == type(MatrixGraph()):
                pass

        return False

    def __len__(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        return len(self.__internal_dict)

    def __str__(self) -> str:
        """
        Gets string representation of Graph
        """
        ans = ''
        for vertice in self.__internal_dict:
            ans += str(vertice) + ' : ' + str(self.__internal_dict[vertice]) + '\n'
        return ans[:-1]
    
    def insert_vertex(self, vertex, edges) -> bool:
        """
        Insert a vertex into the graph
        """
        self.__internal_dict[str(vertex)] = set([str(_) for _ in edges])
        self.__edges += len(edges)
        for edge in edges:
            if str(edge) in self.__internal_dict:
                self.__internal_dict[str(edge)].add(str(vertex))
            else:
                self.__internal_dict[str(edge)] = set([])
        return True
 
    def insert_edge(self, vertex1, vertex2) -> bool:
        """
        Insert an edge between two given vertices
        """
        if not str(vertex1) in self.__internal_dict or not str(vertex2) in self.__internal_dict:
            return False
        self.__edges += 1
        self.__internal_dict[str(vertex1)].add(str(vertex2))
        return True

    def remove_vertex(self, vertex) -> bool:
        """
        Remove a vertex from the graph
        """
        if str(vertex) not in self.__internal_dict:
            return False
        self.__edges -= len(self.__internal_dict[str(vertex)])
        for other_vertex in self.__internal_dict[str(vertex)]:
            self.__internal_dict[other_vertex].remove(str(vertex))
        del self.__internal_dict[str(vertex)]
        return True

    def remove_edge(self, vertex1, vertex2) -> bool:
        """
        Remove a edge from the graph
        """
        if vertex1 in self and vertex2 in self:
            if str(vertex2) not in self.__internal_dict[str(vertex1)]:
                return
            self.__edges -= 1
            self.__internal_dict[str(vertex1)].remove(str(vertex2))
            self.__internal_dict[str(vertex2)].remove(str(vertex1))
            return True
        
        return False
        
    def connection_exists(self, vertex1, vertex2) -> bool:
        """
        Determine whether there is an edge between two vertices
        """
        if vertex1 in self and vertex2 in self:
            return str(vertex2) in self.__internal_dict[str(vertex1)]
        
        return False

    def get_edges(self, vertex):
        """
        Gets all edges from a vertex
        """
        if str(vertex) in self.__internal_dict:
            return list(self.__internal_dict[str(vertex)])
        return []

    def num_edges(self) -> int:
        """
        Gets number of edges in the Graph
        """
        return self.__edges

    def get_vertices(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        return len(self.__internal_dict)

class MatrixGraph(Graph):
    def __init__(self):
        """
        Initialization method
        """
        pass 

    def __iter__(self):
        """
        Iterates through the vertices of the Graph
        """
        pass 

    def __next__(self):
        """
        Assists __iter__ going through the vertices of the Graph
        """
        pass 

    def __eq__(self, other) -> bool:
        """
        Determines if one Graph is the logical equivalent of another
        """
        pass 

    def __len__(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        pass 

    def __str__(self) -> str:
        """
        Gets string representation of Graph
        """
        pass
    
    def insert_vertex(self, vertex, edges) -> bool:
        """
        Insert a vertex into the graph
        """
        pass

    def insert_edge(self, vertex1, vertex2) -> bool:
        """
        Insert an edge between two given vertices
        """
        pass

    def remove_vertex(self, vertex) -> bool:
        """
        Remove a vertex from the graph
        """
        pass

    def remove_edge(self, vertex1, vertex2) -> bool:
        """
        Remove a edge from the graph
        """
        pass

    def connection_exists(self, vertex1, vertex2) -> bool:
        """
        Determine whether there is an edge between two vertices
        """
        pass
    
    def get_edges(self, vertex):
        """
        Gets all edges from a vertex
        """
        pass

    def num_edges(self) -> int:
        """
        Gets number of edges in the Graph
        """
        pass

    def get_vertices(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        pass

if __name__ == '__main__':
    main()

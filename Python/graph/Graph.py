from _interfaces import Graph

def main():
    adj = AdjacencyGraph()
    mat = MatrixGraph()

class AdjacencyGraph(Graph):
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

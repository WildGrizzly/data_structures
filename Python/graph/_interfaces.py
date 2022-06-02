from abc import ABCMeta, abstractmethod

class Graph(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'insert_vertex') and
                callable(subclass.insert_vertex) and
                hasattr(subclass, 'insert_edge') and
                callable(subclass.insert_edge) and
                hasattr(subclass, 'remove_vertex') and
                callable(subclass.remove_vertex) and
                hasattr(subclass, 'remove_edge') and
                callable(subclass.remove_edge) and
                hasattr(subclass, 'connection_exists') and
                callable(subclass.connection_exists) and
                hasattr(subclass, 'get_edges') and
                callable(subclass.get_edges) and
                hasattr(subclass, 'num_vertices') and
                callable(subclass.num_vertices) and
                hasattr(subclass, 'num_edges') and
                callable(subclass.num_edges) and
                hasattr(subclass, '__init__') and
                callable(subclass.__init__) and
                hasattr(subclass, '__iter__') and
                callable(subclass.__iter__) and
                hasattr(subclass, '__eq__') and
                callable(subclass.__eq__) and
                hasattr(subclass, '__len__') and
                callable(subclass.__len__) and
                hasattr(subclass, '__str__') and
                callable(subclass.__str__))

    @abstractmethod
    def insert_vertex(self, vertex, edges) -> bool:
        """
        Insert a vertex into the graph
        """
        raise NotImplementedError

    @abstractmethod
    def insert_edge(self, vertex1, vertex2) -> bool:
        """
        Insert an edge between two given vertices
        """
        raise NotImplementedError

    @abstractmethod
    def remove_vertex(self, vertex) -> bool:
        """
        Remove a vertex from the graph
        """
        raise NotImplementedError

    @abstractmethod
    def remove_edge(self, vertex1, vertex2) -> bool:
        """
        Remove a edge from the graph
        """
        raise NotImplementedError

    @abstractmethod
    def connection_exists(self, vertex1, vertex2) -> bool:
        """
        Determine whether there is an edge between two vertices
        """
        raise NotImplementedError

    @abstractmethod
    def get_edges(self, vertex):
        """
        Gets all edges from a vertex
        """
        raise NotImplementedError

    @abstractmethod
    def num_edges(self) -> int:
        """
        Gets number of edges in the Graph
        """
        raise NotImplementedError

    @abstractmethod
    def get_vertices(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        raise NotImplementedError

    @abstractmethod
    def __init__(self):
        """
        Initialization method
        """
        raise NotImplementedError

    @abstractmethod
    def __iter__(self):
        """
        Iterates through the vertices of the Graph
        """
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other) -> bool:
        """
        Determines if one Graph is the logical equivalent of another
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Gets number of vertices in the Graph
        """
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        """
        Gets string representation of Graph
        """
        raise NotImplementedError

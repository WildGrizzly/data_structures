def main():
    t = Heap(_class = int)

class Heap:
    """
    A linked Heap implmentation
    """
    class __Node:
        """
        Internal node for the heap
        """
        def __init__(self, data, parent=None, leftChild=None, rightChild=None):
            """
            Internal Node constructor
            """
            self.data = data
            self.parent = parent
            self.leftChild = leftChild
            self.rightChild = rightChild

    def __init__(self, minHeap = True, _class = None):
        """
        Constructor for the heap
        minHeap: allows user to make heap a min or max heap
        _class: allows user to enforce type on insertions
        """
        self.min = minHeap
        self.len = 0
        if _class:
            try:
                _class() >= _class()
                _class() <= _class()
                _class() == _class()
            except:
                raise Exception("Class for heap isn't comparable")
        self._class = _class
        self.__top = None

    def add(self, item):
        if self.len == 0:
            self.__top = self.__Node(item)
            return
        

    def __heapify(self, node):
        
        if node == self.__top:

    def pop(self):
        """
        Pop item off the top of the heap
        """
        if not self.len:
            raise Exception("Popping off empty heap")
        

    def peek(self):
        """
        View item at the top of the heap
        """
        if not self.len:
            raise Exception("Peeking at empty heap")
        return self.__top.data
        

if __name__ == "__main__":
    main()

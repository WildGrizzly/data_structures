def main():
    t = LinkedList(int)
    print(t)
    if not t:
        print("Empty or None")
    # t = []
    t.insert_to_back(10)
    t.insert_to_back(12)
    t.insert_to_front(5)
    # t = [5, 10, 12]
    print(t)
    t.delete_index(2)
    t.delete_item(10)
    try:
        t.insert_to_front('hello')
    except:
        print('No strings allowed')
    # t = [5]
    print(t)
    t.insert_to_front(15)
    # t = [15, 5]
    print(t)

class LinkedList:
    """
    This is a simple DLL implementation in Python
    This uses optional type checking on insertions to 
    keep items in the LinkedList the same type.
    """
    class __Node:
        """
        Private Node inner class of the LinkedList
        """
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right


    def __init__(self, _class = None):
        """
        Constructor for the LinkedList class
        """
        self._class = _class
        self.__length = 0
        self.__head = self.__Node()
        self.__tail = self.__Node(left=self.__head)
        self.__head.right = self.__tail

    def clear(self):
        """
        Resets the list to be used again
        """
        self.__length = 0
        self.__head = self.__Node()
        self.__tail = self.__Node(left=self.__head)
        self.__head.right = self.__tail

    def __bool__(self):
        """
        The truthiness of the LinkedList
        """
        return self.__length != 0

    def __len__(self):
        """
        Returns the length of the linked list
        """
        return self.__length

    def __iter__(self):
        """
        Allows the linkedlist to be iterable many times
        """
        self.__list_runner = self.__head
        return self

    def __next__(self):
        """
        Defines how to get the next item in the iteration
        """
        if self.__list_runner.right != self.__tail:
            self.__list_runner = self.__list_runner.right
            return self.__list_runner.data
        else:
            raise StopIteration

    def __str__(self):
        """
        Returns string representation of the linked list
        """
        if not self:
            return '[]'
        ans = '['
        for ele in self:
            ans += f'{str(ele)}, '
        return ans[:-2] + ']'

    def insert_to_back(self, item):
        """
        Placing an item in the back of LinkedList
        """
        if self._class and not isinstance(item, self._class):
            raise ValueError(f"{item} is not of type: {self._class}")
        self.__length+=1
        new_node = self.__Node(item, self.__tail.left, self.__tail)
        self.__tail.left.right = new_node
        self.__tail.left = new_node
        
    
    def insert_to_front(self, item):
        """
        Placing an item at the front of LinkedList
        """
        if self._class and not isinstance(item, self._class):
            raise ValueError(f"{item} is not of type: {self._class}")
        self.__length+=1
        new_node = self.__Node(item, self.__head, self.__head.right)
        self.__head.right.left = new_node
        self.__head.right = new_node


    def delete_index(self, ind: int):
        """
        Deleting item ar known index
        Can be used to pop items from head or tail
        delete_index(0), delete_index(len(list) - 1)
        """
        if ind < 0 or ind >= self.__length:
            raise Exception(f"Index:{ind}, out of the bounds of LinkedList")
        from_back = ind >= (self.__length / 2)
        self.__length-=1
        if from_back:
            runner = self.__tail.left
            for i in range(self.__length - ind):
                runner = runner.left
        else:
            runner = self.__head.right
            for i in range(ind):
                runner = runner.right
        runner.left.right = runner.right
        runner.right.left = runner.left
        return runner.data


    def delete_item(self, item):
        """
        Seaches list to eliminate item
        """
        if self._class and not isinstance(item, self._class):
            return
        runner = self.__head.right
        for i in range(self.__length):
            if runner.data == item:
                break
            runner = runner.right
        if runner == self.__tail:
            return
        self.__length-=1
        runner.left.right = runner.right
        runner.right.left = runner.left
        return runner.data
        

    def item_at_index(self, ind: int):
        """
        Returns item at the respective index
        """
        if ind < 0 or ind >= self.__length:
            raise Exception(f"Index:{ind}, out of the bounds of LinkedList")
        from_back = ind >= (self.__length / 2)
        runner = None
        if from_back:
            runner = self.__tail.left
            for i in range(self.__length - ind):
                runner = runner.left
        else:
            runner = self.__head.right
            for i in range(ind):
                runner = runner.right

        return runner.data


if __name__ == "__main__":
    main()

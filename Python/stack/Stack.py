from linked_list.LinkedList import LinkedList

def main():
    t = Stack(int)
    t.push(10)
    t.push(11)
    t.push(12)
    print(t.peek())
    print(t)
    print(f"{t.pop()}, {t.pop()}")
    print(t)
    print(t.pop())

class Stack(LinkedList):
    """
    This is a linked stack implementation
    """
    def peek(self):
        """
        Returns item at the top of the stack without removing
        """
        return self.item_at_index(0)        


    def pop(self):
        """
        Pops the item at the top of the stack
        """
        if not self.len:
            raise Exception("Popping from empty Stack")
        return self.delete_index(0)


    def push(self, item):
        """
        Pushes an item to the top of the stack
        """
        self.insert_to_front(item)


if __name__ == "__main__":
    main()

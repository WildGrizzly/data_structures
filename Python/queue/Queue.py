from LinkedList import LinkedList

def main():
    t = Queue(int)
    t.enqueue(5)
    t.enqueue(6)
    t.enqueue(20)
    print(t)
    print(t.dequeue())
    print(t.peek())
    t.dequeue()
    t.dequeue()
    print(t)
    #t.dequeue()


class Queue(LinkedList):
    """
    This is a basic linked queue iomplementation
    """
    def enqueue(self, item):
        """
        Places an item on the queue
        """
        return self.insert_to_back(item)

    def dequeue(self):
        """
        Removes an item from the queue
        """
        if not self.len:
            raise Exception("Dequeueing from empty queue")
        return self.delete_index(0)

    def peek(self):
        """
        Returns next item in the queue without removing it
        """
        return self.item_at_index(self.len - 1)


if __name__ == "__main__":
    main()


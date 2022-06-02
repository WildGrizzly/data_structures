
def main(): 
    test = Dictionary()
    print(test)
    print("test[4] = 'hello'")
    test[4] = 'hello'
    print("test[5] = 'delete'")
    test[5] = 'delete'
    print("test['hello'] = 4")
    test['hello'] = 4
    print("test[4] = wanker")
    test[4] = 'wanker'
    print('del test[5]')
    del test[5]
    print(test)
    if 4 in test:
        print('4 in test: True')
    else:
        print('4 in test: False')
    if 5 in test:
        print('5 in test: True')
    else:
        print('5 in test: False')

    for i, key in enumerate(test):
        print(f'key {i}: {key}')
    print(f'Length: {len(test)}')

class Tombstone:
    def __eq__(self, other):
        return type(other) == type(self)

class Dictionary:
    def __init__(self, length=53):
        self.__internal_array = [None] * length
        self.__key_list = DLL()
        self.__num_tombstones = 0

    def __setitem__(self, key, value):
        ind = self.__index(key)
        # New Entry
        node = self.__key_list.insert(key)
        if self.__internal_array[ind] is None:
            self.__internal_array[ind] = (value, node, key)
            return

        if key == self.__internal_array[ind][2]:
            self.__key_list.delete(self.__internal_array[ind][1])
            self.__internal_array[ind] = (value, node, key)
            return

        # Hash collision
        new_ind = self.__hash_collision_policy(ind, key)
        self.__internal_array[new_ind] = (value, node, key)

    def __getitem__(self, key):
        if key not in self:
            raise Exception(f'Key not in dictionary: {key}')
        ind = self.__index(key)
        if key == self.__internal_array[ind][2]:
            return self.__internal_array[ind][0]
        ind = self.__hash_collision_policy(ind, key)
        if not ind:
            return
        return self.__internal_array[ind][0]
        
    def __hash_collision_policy(self, curr_ind, key):
        quadratic_probe = 1
        ind = curr_ind
        counter = 0
        while self.__internal_array[ind] is None or self.__internal_array[ind] == Tombstone() or self.__internal_array[ind][2] != key:
            ind += quadratic_probe ** 2
            ind = ind % len(self.__internal_array)
            quadratic_probe += 1
            counter += 1
            if counter > len(self.__internal_array) // 2:
                counter = -1
                break
        if counter == -1:
            return None
        return ind

    def __delitem__(self, key):
        if key not in self:
            return
        ind = self.__index(key)
        if self.__internal_array[ind][2] != key:
            ind = self.__hash_collision_policy(ind, key)
            if not ind:
                return

        node = self.__internal_array[ind][1]
        self.__key_list.delete(node)
        self.__internal_array[self.__index(key)] = Tombstone()
        self.__num_tombstones += 1

    def __contains__(self, key):
        ind = self.__index(key)
        if self.__internal_array[ind] is None:
            return False
        if self.__internal_array[ind] == Tombstone() or self.__internal_array[ind][2] != key:
            ind = self.__hash_collision_policy(ind, key)
            if not ind:
                return False

        return True

    def __index(self, key):
        return hash(key) % len(self.__internal_array)

    def __len__(self):
        return len(self.__key_list)

    def __iter__(self):
        self.__key_list_runner = self.__key_list.head
        return self

    def __next__(self):
        if self.__key_list_runner.next != self.__key_list.tail:
            self.__key_list_runner = self.__key_list_runner.next
            return self.__key_list_runner.value
        else:
            raise StopIteration
    
    def __str__(self):
        if not len(self):
            return '{}'
        ans = "{"
        for key in self.__key_list:
            ans += f'{key} : {self[key]}, '
        return ans[:-2] + '}'

class Node:
    def __init__(self, v = None, n = None, p = None):
        self.value = v
        self.next = n
        self.previous = p

    def __str__(self):
        if not self.value:
            raise Exception('Node string converstion out of bounds')
        if self.next.value == None and self.previous.value == None:
            return f'Node({self.value}, TAIL, HEAD)'
        if self.next.value == None:
            return f'Node({self.value}, TAIL, {self.previous.value})'
        if self.previous.value == None:
            return f'Node({self.value}, {self.next.value}, HEAD)'
        return f'Node({self.value}, {self.next.value}, {self.previous.value})'

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node(p=self.head)
        self.head.next = self.tail
        self.size = 0

    def insert(self, item):
        last_item = self.tail.previous
        new_node = Node(item, self.tail, last_item)
        last_item.next = new_node
        self.tail.previous = new_node
        self.size += 1
        return new_node

    def delete(self, node):
        if not node:
            return
        if not node.previous or not node.next:
            raise Exception(f"Out of bounds deletion {node}")

        prev = node.previous
        prev.next = node.next
        node.next.previous = prev

        self.size -= 1

    def __iter__(self):
        self.__iterator_runner = self.head
        return self

    def __next__(self):
        if self.__iterator_runner.next != self.tail:
            self.__iterator_runner = self.__iterator_runner.next
            return self.__iterator_runner.value
        else:
            raise StopIteration
    
    def __len__(self):
        return self.size

    def __str__(self):
        ans = ""
        for ele in self:
            ans += str(ele) + " -> "
        return ans[:-4]

if __name__ == "__main__":
    main()

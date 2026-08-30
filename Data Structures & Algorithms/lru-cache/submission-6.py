class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.capacity = capacity
        self.cachemap = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node

    def insert_at_front(self, node):
        # create new link of new node
        node.prev = self.head
        node.next = self.head.next
        # remove existing links
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int) -> int:
        if key not in self.cachemap:
            return -1
        node = self.cachemap[key]
        # remove (delink) from original position and insert in start
        self.remove(node)
        self.insert_at_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            node = self.cachemap[key]

            node.val = value
            self.remove(node)
            self.insert_at_front(node)

        else:
            new_node = Node(key, value)

            self.insert_at_front(new_node)
            self.cachemap[key] = new_node

            if len(self.cachemap) > self.capacity:
                last_node = self.tail.prev

                self.remove(last_node)
                del self.cachemap[last_node.key]

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {}
        # initially dummy node
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
        node = self.cache_map[key]
        self.remove(node)
        self.insert_at_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            node = self.cache_map[key]
            node.val = value
            self.remove(node)
            self.insert_at_front(node)
        else:
            new_node = Node(key,value)
            self.insert_at_front(new_node)
            self.cache_map[new_node.key] = new_node
            # if capacity exceed
            if len(self.cache_map) > self.capacity:
                last_node = self.tail.prev
                self.tail.prev = last_node.prev
                last_node.prev.next = self.tail
                del self.cache_map[last_node.key]

        

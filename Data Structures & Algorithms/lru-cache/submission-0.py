class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert node at the MRU position (before tail)
    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)
            return

        # Create new node
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Remove LRU if capacity exceeded
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

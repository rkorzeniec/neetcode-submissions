class Node:
    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.cache: dict[int, Node] = {}
        self.max_capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self._remove_node(self.cache[key])
        self._add_to_tail(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        node = Node(key, value)

        self.cache[key] = node

        if len(self.cache) > self.max_capacity:
            lru_node = self.head.next
            self._remove_node(lru_node)
            del self.cache[lru_node.key]
            
        self._add_to_tail(node)

    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node

        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
class LRUNode:
    def __init__(self, key, value) -> object:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head =LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None
    
    def post(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node  =LRUNode(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node_to_remove = self.head.next
            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]        

    # prev <----> node <-----> tail
    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

def main():
    cache = LRUCache(3)
    cache.post("k1", 'v1')
    cache.post("k2", 'v2')
    cache.post("k3", 'v3')
    print(cache.get('k1'))
    print(cache.get('k2'))
    print(cache.get('k3'))
    print("\n\n")
    cache.post('k', 'k4')
    print(cache.get('k1'))
    print("\n\n")

if __name__ == '__main__':
    main()
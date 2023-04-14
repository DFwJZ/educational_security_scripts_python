class LRUNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    Implement a Least Recently Used (LRU) cache with a fixed capacity.
    The cache supports get and put operations with O(1) time complexity.
    When the cache reaches its capacity, it will evict the least recently used item.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = LRUNode(None, None)
        self.tail = LRUNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        # Retrieve the value associated with the given key if it exists in the cache.
        # If the key is not found in the cache, return None.
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None
    
    def put(self, key, value):
        # Add or update the key-value pair in the cache.
        # If the cache is full, evict the least recently used item before adding the new key-value pair.
        if key in self.cache:
            self._remove(self.cache[key])
        node = LRUNode(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node_to_remove = self.head.next
            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]
            
    def _remove(self, node):
        # Remove a node from the doubly linked list.
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add(self, node):
         # Add a node to the end of the doubly linked list, right before the tail.
        prev_node = self.tail.prev
        prev_node.next = node
        node.next = self.tail
        node.prev = prev_node
        self.tail.prev = node

def main():
    cache = LRUCache(3)
    cache.put("API_KEY_1", "api_key_value_1")
    cache.put("API_KEY_2", "api_key_value_2")
    cache.put("API_KEY_3", "api_key_value_3")

    print(cache.get("API_KEY_1"))  # Output: api_key_value_1
    print(cache.get("API_KEY_2"))  # Output: api_key_value_2

    cache.put("API_KEY_4", "api_key_value_4")

    print(cache.get("API_KEY_3"))  # Output: None (evicted)
    print(cache.get("API_KEY_4"))  # Output: api_key_value_4

if __name__ == "__main__":
    main()
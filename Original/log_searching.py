class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, pattern):
        def _search(node, pattern, path):
            if not pattern:
                
                if node.is_end_of_word:
                    results.append("".join(path))
                return

            char = pattern[0]
            # print(char)
            if char in node.children:  
                print(pattern[1:])
                _search(node.children[char], pattern[1:], path + [char])

        results = []
        _search(self.root, pattern, [])
        return results

    def search(self, pattern):
        
        def _search(node, pattern, path):
            if not pattern:
                if node.is_end_of_word:
                    result.append("".join(path))
                return
            
            char = pattern[0]
            if char in node.children:
                _search(node.children[char], pattern[1:], path + [char])


        result = []
        _search(self.root, pattern, [])
        return result




    def __str__(self):
        def _traverse(node, path):
            if node.is_end_of_word:
                results.append("".join(path))

            for char, child in node.children.items():
                _traverse(child, path + [char])

        results = []
        _traverse(self.root, [])
        return "\n".join(results)
    
def main():
    log_data = [
        "Login attempt failed",
        "User logged in",
        "Password changed",
        "Login attempt failed",
        "User logged out",
        "Login attempt failed",
    ]

    trie = Trie()
    for entry in log_data:
        trie.insert(entry)

    print(trie)
    search_pattern = "User logged out"
    matched_logs = trie.search(search_pattern)
    print(f"Logs matching pattern '{search_pattern}':")
    for log in matched_logs:
        print(log)

if __name__ == "__main__":
    main()

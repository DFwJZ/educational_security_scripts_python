from collections import defaultdict
from cryptography.fernet import Fernet

class SecureKeyValueStore():
    def __init__(self, encryption_key = None):
        self.store = defaultdict(str)
        if encryption_key is None:
            self.__encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.__encryption_key)

    def get(self, key):
        encryption_value = self.store.get(key)
        if encryption_value:
            return self.fernet.decrypt(self.store[key]).decode()
        return None
    
    def put(self, key, value):
        self.store[key] = self.fernet.encrypt(value.encode())

    def delete(self, key):
        if key in self.store:
            del self.store[key]


def main():
    key_pair = SecureKeyValueStore()
    key_pair.put('k1', 'v1')
    key_pair.put('k2', 'v2')

    print(key_pair.get('k1'))

    key_pair.delete('k1')
    print(key_pair.get('k1'))



if __name__ == '__main__':
    main()
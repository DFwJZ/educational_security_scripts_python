from collections import defaultdict
from cryptography.fernet import Fernet


class SecureKeyValueStore:
    """
    Implement a secure key-value store:
    Design a secure key-value store with functions such as put(key, value), get(key), 
    and delete(key). Ensure that the data is encrypted while at rest, and
    
    """
    def __init__(self, encryption_key=None):
        self.__store = defaultdict(str)
        if encryption_key is None:
            self.__encryption_key = Fernet.generate_key()
        self.fernet = Fernet(self.__encryption_key)

    def put(self, key, value):
        # Add or update a key-value pair in the store, with the value encrypted.
        self.__store[key] = self.fernet.encrypt(value.encode())

    def get(self, key):
        # Retrieve the value associated with the given key, decrypting it before returning.
        # If the key is not found in the store, return None.
        encrypted_value = self.__store.get(key)
        if encrypted_value:
            return self.fernet.decrypt(self.__store[key]).decode()
        return None

    def delete(self, key):
        # Remove a key-value pair from the store, if it exists.
        if key in self.__store:
            del self.__store[key]

def main():
    store = SecureKeyValueStore()
    store.put('key1', 'val1')
    print(store.__store['key1'])

    print(store.get('key1'))
    print(store.get('sdaf'))
    store.put('sdaf', 'val2')
    print(store.get('sdaf'))
    store.delete('sdaf')
    print(store.get('sdaf'))

if '__main__' == __name__:
    main()
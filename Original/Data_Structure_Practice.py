# Linked list

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, value):
        new_node = LinkedListNode(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def del_head(self):
        if self.head:
            self.head = self.head.next

    def del_tail(self):
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None

    def __str__(self) -> list:
        elements = []
        if not self.head:
            return None
        else:
            current = self.head
            while current:
                elements.append(str(current.value))
                current = current.next
        return '->'.join(elements)

        
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(str(item))
    
    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def is_empty(self) -> bool:
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        ls = []
        if self.is_empty():
            return None
        
        for i in range(len(self.items)):
            ls.append(str(self.items[i]))
        return '->'.join(ls)




def main():
    # # Linkedlist
    # ll = LinkedList()
    # ll.insert_head(234)
    # ll.insert_head(1)
    # ll.insert_head(2)
    # ll.insert_tail(321)
    # print(ll)

    # Stack
    stk = Stack()
    stk.push("sff")
    stk.push("13")
    stk.push(LinkedListNode(123))
    print(f"bot | {stk} | top")


if __name__ == '__main__':
    main()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, data):
        current = self.head
        if current is None:
            raise ValueError("Value not found in list")
        if current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            raise ValueError("Value not found in list")
        prev.next = current.next

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After insertions:", ll.traverse())
    ll.delete_value(20)
    print("After deleting 20:", ll.traverse())
    ll.delete_value(10)
    print("After deleting 10:", ll.traverse())
    ll.delete_value(30)
    print("After deleting 30:", ll.traverse())
    try:
        ll.delete_value(40)
    except ValueError as e:
        print("Error:", e)
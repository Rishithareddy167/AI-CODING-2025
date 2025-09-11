class QueueList:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    q = QueueList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Dequeue:", q.dequeue())  
    print("Dequeue:", q.dequeue())  
    print("Is empty?", q.is_empty())  
    print("Dequeue:", q.dequeue())  
    print("Is empty?", q.is_empty())
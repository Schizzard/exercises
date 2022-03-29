class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())
print(q.dequeue())

pass

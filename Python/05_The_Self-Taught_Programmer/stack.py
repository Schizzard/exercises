class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


# just test
a = Stack()
print(a.is_empty())
a.push(1)
print(a.is_empty())
last_item = a.pop()
pass

# reverse str with stack
stack = Stack()
target = 'Привет'
reverse_str = ""

for l in target:
    stack.push(l)

for i in range(stack.size()):
    reverse_str += stack.pop()

print(reverse_str)

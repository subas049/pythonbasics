class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if len(self.queue) < 10:
            self.queue.append(data)
        else:
            print("Error: Queue is Full")

    def dequeue(self):
        if len(self.queue) == 0:
            return "Error: Queue is Empty"
        return self.queue.pop(0)

    def front_item(self):
        if len(self.queue) == 0:
            return "Error: Queue is Empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q1=Queue()
print(q1.is_empty())
print(q1.size())
print(q1.front_item())
print(q1.dequeue())
for i in range(10):
    q1.enqueue(i)
print(q1.queue)
q1.enqueue(56)
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.queue)
q1.enqueue(49)
print(q1.queue)

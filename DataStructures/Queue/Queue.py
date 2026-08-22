class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
            """Print all values in the queue from first to last."""
            temp = self.first
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print(f"Queue :  {', '.join(values)}")

    def enqueue(self, value): # O(1)
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else: 
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return True

    def dequeue(self): # O(1)
        if self.length == 0 :
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


queue = Queue(21)

queue.enqueue(20)
queue.enqueue(7)
queue.enqueue(4)

queue.print_queue()

print(queue.dequeue().value)
print(queue.dequeue().value)

queue.print_queue()

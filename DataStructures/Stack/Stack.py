class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: 
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        """Print all values in the stack from top to bottom."""
        temp = self.top
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(f"Stack :  {', '.join(values)}")

    def push(self, value): # O(1)
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self): # O(1)
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        if self.height == 0:
            self.top = None
        return temp


stack = Stack(21)
stack.push(3)
stack.push(7)
stack.push(45)
stack.push(10)
stack.print_stack()

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)

stack.print_stack()

        
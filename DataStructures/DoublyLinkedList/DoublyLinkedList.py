class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(f"Doubly Linked List:  {', '.join(values)}")


    def append(self, value): # O(1)
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value): # O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop(self): # O(1)
        if self.length == 0:
            return None
        temp = self.tail
        if self.length > 1:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self): # O(1)
        if self.length == 0:
            return None
        temp = self.head
        if self.length > 1:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get_value(self, index): # O(n)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, value, index): # O(n)
        temp = self.get_value(index)
        temp.value = value
        return True

    def insert_value(self, value, index): # O(n)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get_value(index-1)
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        
        self.length += 1
        return True

    def remove_value(self, index): # O(n)
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length-1:
            return self.pop()

        prev = self.get_value(index-1)
        temp = prev.next
        next = temp.next
        prev.next = next
        next.prev = prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
            

# Creating a Doubly Linked List with Initial Node : 20
doubly_linked_list = DoublyLinkedList(20)

# Adding new elements to Doubly Linked List at the end 
doubly_linked_list.append(7)
doubly_linked_list.append(4)

# Adding new elements to Doubly Linked List at the beginning
doubly_linked_list.prepend(21)
doubly_linked_list.prepend(3)
doubly_linked_list.print_list()

# Removing the last element from the Doubly Linked List
print(doubly_linked_list.pop().value)

# Removing the first element from the Doubly Linked List
print(doubly_linked_list.pop_first().value)

doubly_linked_list.print_list()

# get the last element from the Doubly Linked List by index
print(doubly_linked_list.get_value(2).value)

# set the last element in the Doubly Linked List by index, value
doubly_linked_list.set_value(4, 2)

doubly_linked_list.print_list()

# Inserting the element to the Doubly Linked List at certain index
doubly_linked_list.insert_value(36, 1)

doubly_linked_list.print_list()

# Removing the element from the Doubly Linked List at certain index
print(doubly_linked_list.remove_value(2).value)

doubly_linked_list.print_list()


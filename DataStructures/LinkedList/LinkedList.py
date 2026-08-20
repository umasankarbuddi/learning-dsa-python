
class Node:
    """Store a value and a reference to the next node."""

    def __init__(self, value):
        """Create a node with no next node."""
        self.value = value
        self.next = None

class LinkedList:
    """Manage an ordered collection of linked nodes."""

    def __init__(self, value):
        """Create a linked list containing one initial value."""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print all values in the list from head to tail."""
        temp = self.head
        values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(f"Linked List:  {', '.join(values)}")

    def append(self, value): # O(1)
        """Add a value to the end of the list and return True."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value): # O(1)
        """Add a value to the beginning of the list and return True."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self): # O(n)
        """Remove and return the last node, or None if the list is empty."""
        if self.length == 0:
            return None
        temp = self.head
        pre = temp
        while temp.next is not None:
            pre = temp
            temp = temp.next
        pre.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self): # O(1)
        """Remove and return the first node, or None if the list is empty."""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        """Return the node at index, or None when the index is invalid."""
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, value, index):
        """Update a node's value and return True, or False for an invalid index."""
        if index < 0 or index >= self.length:
            return False
        node = self.get(index)
        node.value = value
        return True

    def insert(self, value, index):
        """Insert a value at index and return True, or False for an invalid index."""
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Remove and return the node at index, or None for an invalid index."""
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

        


# Creating a Linked List with Initial Node : 21
linkedList = LinkedList(21)

# Adding a new element to linked list using prepend method
linkedList.prepend(45)
linkedList.prepend(4)

# Adding a new element to the linked list using append method
linkedList.append(20)
linkedList.append(7)

# Printing the linked list using print_list method
linkedList.print_list()

# Removing the last element of the linked list using pop method
print(linkedList.pop().value)

# Removing the last element of the linked list using pop method
print(linkedList.pop_first().value)

# Getting the element of the linked list of a given index
print(linkedList.get(2).value)

# Setting the element of the linked list of a given index with new value
linkedList.set(3, 2)

# Inserting a new element to the linked list at a given index
linkedList.insert(4, 2)

# Removing the element of the linked list at a given index
print(linkedList.remove(3).value)






class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return 1
        while current and counter <= position:
            if counter == position:
                return current

            else:
                current = current.next
                counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter <= position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = None

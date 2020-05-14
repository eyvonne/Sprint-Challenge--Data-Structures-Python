class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return f'{self.value}'

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if node:
            if not node.next:
                self.head = node
                node.next = prev
                print(node)
            else:
                self.reverse_list(node.next, node)
                node.next = prev
                print(node)

    def print_list(self):
        if self.head == None:
            print(None)
            return None
        current = self.head
        while current != None:
            print(current)
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_to_head(3)
    ll.add_to_head(2)
    ll.add_to_head(1)
    ll.reverse_list(ll.head, None)

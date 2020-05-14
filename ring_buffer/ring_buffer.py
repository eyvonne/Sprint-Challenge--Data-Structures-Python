class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, node):
        self.next = node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buffer = None

    def append(self, item):
        if self.size < self.capacity:
            if not self.buffer:
                self.buffer = Node(item)
                self.tail = self.buffer
            else:
                self.buffer.set_next(Node(item))
                self.buffer = self.buffer.next
            self.size += 1
            if self.size == self.capacity:
                self.buffer.set_next(self.tail)

        else:
            self.buffer.next.set_value(item)
            self.buffer = self.buffer.next

    def get(self):
        l = []
        for i in range(self.size):
            l.append(self.tail.get_value())
            self.tail = self.tail.next
        return l


if __name__ == '__main__':
    buffer = RingBuffer(3)

    print(buffer.get())   # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    print(buffer.buffer.value)
    print(buffer.get())   # should return ['a', 'b', 'c']
    print(buffer.buffer.value)
    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    print(buffer.get())   # should return ['d', 'b', 'c']

    buffer.append('e')
    buffer.append('f')

    print(buffer.get())

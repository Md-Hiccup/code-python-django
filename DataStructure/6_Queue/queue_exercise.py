from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[0]

def place_order(orders):
    pass

def server_order(orders):
    pass

if __name__ == "__main__":
    # Producer-Consumer problem
    # where place_order is producing orders
    # and server_order is consuming orders
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

    # Print binary number from 1-10

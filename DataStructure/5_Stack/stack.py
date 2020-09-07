from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


if __name__ == "__main__":

    s = Stack()
    s.push(5)
    s.push(45)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.is_empty())



    # List
    s = []
    s.append('https://www.cnn.com/')
    s.append('https://www.cnn.com/world')
    s.append('https://www.cnn.com/india')
    s.append('https://www.cnn.com/china')

    print('pop last element:', s.pop())


    # Deque
    stack = deque()
    # to check method of stack
    print(dir(stack))
    stack.append('https://www.cnn.com/')
    stack.append('https://www.cnn.com/world')
    stack.append('https://www.cnn.com/india')
    stack.append('https://www.cnn.com/china')
    print(stack)
    print(stack.pop())
    print(stack)


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

# Reverse string using Stack class
def reverse_string(sentence):
    stk = Stack()
    for ch in sentence:
        stk.push(ch)

    rstr = ''
    while(not stk.is_empty()):
        rstr += stk.pop()

    return rstr

# Check if parenthesis is in the string are balanced or not.
def is_match(ch1, ch2):
    match_dict = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    return match_dict[ch1] == ch2

def is_balanced(string):
    stack = Stack()
    for ch in string:
        if ch == "(" or ch == "[" or ch == "{":
            stack.push(ch)
        if ch == ")" or ch == "]" or ch == "}":
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()):
                return False

    return stack.size() == 0

    # stk = Stack()
    # is_bal = False
    # for ch in string:
    #     if ch == "(" or ch == "[" or ch == "{":
    #         stk.push(ch)
    #
    #     if stk.is_empty():
    #         continue
    #
    #     if ch == ")":
    #         if stk.peek() == "(":
    #             stk.pop()
    #             is_bal = True
    #         else:
    #             is_bal = False
    #     if ch == "]":
    #         if stk.peek() == "[":
    #             stk.pop()
    #             is_bal = True
    #         else:
    #             is_bal = False
    #     if ch == "}":
    #         if stk.peek() == "{":
    #             stk.pop()
    #             is_bal = True
    #         else:
    #             is_bal = False
    # if is_bal:
    #     return True
    #
    # return False



if __name__ == "__main__":
    # 1. Reverse the string
    print(reverse_string("We will conquere COVID-19"))
    print(reverse_string("I am the king"))

    # 2. Paranthesis checker
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
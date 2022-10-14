import sys
import typing


class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value: typing.Union[int, float]):
        """
        Add element to stack
        """
        self.stack.append(value)
        if self.max_stack:
            self.max_stack.append(max(value, self.max_stack[-1]))
        else:
            self.max_stack.append(value)

    def top(self):
        """
        Show top element on stack if stack is not empty
        """
        if self.stack:
            print(self.stack[-1])
        else:
            print('Stack is empty')

    def pop(self):
        """
        Remove top element from stack
        """
        if self.stack:
            self.stack.pop()
            self.max_stack.pop()
        else:
            raise TypeError('stack is empty')

    def max(self):
        """
        Show max element on stack
        """
        if self.stack:
            print(self.max_stack[-1])
        else:
            print('Stack is empty')


def main():
    q = int(sys.stdin.readline())
    my_stack = Stack()

    for _ in range(q):
        request = list(sys.stdin.readline().split())

        if request[0] == 'push':
            my_stack.push(int(request[1]))

        elif request[0] == 'pop':
            my_stack.pop()

        elif request[0] == 'max':
            my_stack.max()

        elif request[0] == 'top':
            my_stack.top()


if __name__ == "__main__":
    main()

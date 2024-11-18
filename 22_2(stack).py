class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0


stack1 = Stack()
print(stack1.stack)  # []
print(stack1.is_empty())  # True
stack1.push('1')
stack1.push('2')
print(stack1.stack)  # ['1', '2']
print(stack1.is_empty())  # False

top_element = stack1.pop()
print(top_element)  # 2
second_element = stack1.pop()
print(second_element)  # 1
class Stack:

    def __init__(self, name):
        self.name = name
        self.stack = []

    def push(self, item):
        self.stack.append(item)


    def peek(self):
        if self.stack:
            return self.stack[-1]

    def pop(self):
        if self.stack:
            top = self.peek()
            del self.stack[-1]
            return top

    # def scan_for_min(self):
    #     min_value = self.stack[0]
    #     for item in self.stack[1:]:
    #         if item < min_value:
    #             min_value = item
    #     self.min = min_value

    # def min(self):
    #     return self.min


class MinStack(Stack):

    def __init__(self, name):
        self.name = name
        self.stack = []
        self.min = None
        self.min_stack = Stack("min stack")

    def push(self, item):
        self.stack.append(item)
        if self.min == None or item <= self.min:
            self.min = item
            self.min_stack.push(item)

    def pop(self):
        if self.stack:
            top = self.peek()
            del self.stack[-1]
            if top == self.min:
                self.min_stack.pop()
                self.min = self.min_stack.peek()
            return top


if __name__ == "__main__":

    my_stack = MinStack("Number Stack")
    my_stack.push(465)
    print(my_stack.min_stack.stack)
    my_stack.push(3)
    print(my_stack.min_stack.stack)
    my_stack.push(9)
    print(my_stack.min_stack.stack)
    my_stack.push(-3843)
    print(my_stack.min_stack.stack)

    print("min:", my_stack.min) # -3843
    print("popped:", my_stack.pop()) # -3843
    print("min:", my_stack.min) # 3

    print("popped:", my_stack.pop()) # 9
    print("min:", my_stack.min) # 3

    print("popped:", my_stack.pop()) # 3
    print("min:", my_stack.min) # 465

    print("popped:", my_stack.pop()) # 465
    print("min:", my_stack.min) # None

    # tos = my_stack.pop() # should give "other thing"
    # print(tos) # "other thing"
    # print(my_stack.pop()) # "thing"
    # print(my_stack.pop()) # None

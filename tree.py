class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        root = f"Root: {self.data}"
        left = f"Left: {self.left} |" if self.left else ""
        right = f"| Right: {self.right}" if self.right else ""
        return f"({left}{root}{right})"
    
    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value) -> bool:
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(f"|{self.data}|", end=" ")
        if self.right:
            self.right.print_in_order()

    def print_post_order(self):
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print(f"|{self.data}|", end=" ")

    def print_pre_order(self):
        print(f"|{self.data}|", end=" ")
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()


test1 = Node(20)
test1.insert(25)
test1.insert(10)
test1.insert(5)
test1.insert(12)
print(test1)
print(test1.contains(8))
test1.print_in_order()
test1.print_post_order()
test1.print_pre_order()
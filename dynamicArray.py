# Implementation
class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def insert(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.data[index] = index


# Interface example
x = Array(size=5)   # this is how I want to create an array
x.insert(0) = 4     # this is how I want to insert an element
print(x.data)       # this is how I want to read the data
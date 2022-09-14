# Implementation
import random

class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None for _ in range(size)]

    def __repr__(self):
        return str(self.data)

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.data[index] = value

    def indexing(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.data[index]


# Interface example
x = Array(size=10)   # this is how I want to create an array
for i in range(10):
    x.insert(index=i, value=random.randint(1, 100))

for i in range(10):
    print(x.indexing(index=i))

print(x)       # this is how I want to read the data

def test1():
    count = 0

    for z in range(3):
        print(f"\nz{z + 1}")
        
        for _ in range(5):
            for _ in range(5):
                print(count, end=" ")
                count += 1
            
            print()

test1()
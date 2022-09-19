# Implementation
import random
from turtle import color

class stack:
    def __init__(self):  # constructor
        self.items = []

    def __repr__(self) -> str:  # string representation
        output = ""
        border_length = 0

        for item in self.items: # generate the stack
            output += self.color(item) + " | "
            border_length += len(str(item)) + 3

        border = "-" * (border_length + 1)

        return f"{border} \n| {output}\n{border}"

    def color(self, item):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return "\x1b[38;2;{r};{g};{b};243m".format(r=r, g=g, b=b)  + str(item) + "\x1b[0m"

    def push(self, item):  # add an item to the end
        self.items.append(item)

    def pop(self):  # remove and return the first item
        self.items = self.items[:-1]
        return self.items

    def isEmpty(self):  # check if the stack is empty
        return self.items == []

# Interface example
s = stack()
print(s.isEmpty())
s.push("China")
s.push("India")
s.push("USA")
s.push("Indonesia")
s.push("Brazil")
s.push("Pakistan")
s.push("Nigeria")
s.push("Bangladesh")
s.push("Russia")
s.push("Mexico")
print(s.isEmpty())
print(s)
s.pop()
print(s)
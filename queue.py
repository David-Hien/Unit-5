# Implementation
class queue:
    def __init__(self):  # constructor
        self.items = []

    def __repr__(self) -> str:  # string representation
        output = ""
        border_length = 0

        for item in self.items: # generate the queue
            output += "\x1b[6;30;42m" + str(item) + "\x1b[0m" + " | "
            border_length += len(str(item)) + 3

        border = "-" * (border_length + 1)

        return f"{border} \n| {output}\n{border}"

    def enqueue(self, item):  # add an item to the end
        self.items.insert(0, item)

    def dequeue(self):  # remove and return the first item
        return self.items.pop()

    def isEmpty(self):  # check if the queue is empty
        return self.items == []


# Interface example
q = queue()
q.enqueue("China")
q.enqueue("India")
q.enqueue("USA")
q.enqueue("Indonesia")
q.enqueue("Brazil")
q.enqueue("Pakistan")
q.enqueue("Nigeria")
q.enqueue("Bangladesh")
q.enqueue("Russia")
q.enqueue("Mexico")

print(q)

for i in range(10):
    print(q.dequeue())
    print(q.isEmpty())

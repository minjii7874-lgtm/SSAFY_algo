class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.left = B
A.right = C
C.left = D
C.right = E


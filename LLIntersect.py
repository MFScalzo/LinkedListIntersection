# Node Class Implementation
class Node:
    data = None
    nextNode = None

    def __init__(self, d: int):
        data = d

# The solution function
def findIntersection(head1: Node, head2: Node):
    nodesSeen = set()

    while (head1 != None):
        nodesSeen.add(head1)
        head1 = head1.nextNode

    while (head2 != None):
        if head2 in nodesSeen:
            return head2

        nodesSeen.add(head2)
        head2 = head2.nextNode

    return None

# BELOW IS ALL TESTING
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.nextNode = C
B.nextNode = C
C.nextNode = D

result = findIntersection(A,B)

# id() to get the address of an object
if id(result) == id(C):
    print("Intersection found at Node: " + str(C))

if id(result) == id(None):
    print("No intersection found.")
from llist import LList, Node, append

# Nastia Yermishyna #

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LList:
    def __init__(self):
        self.head = None

def append(lst, newnode):
    """append newnode to a finite linked list lst"""
    if lst.head:
        node = lst.head
        while node.next:
            node = node.next
        node.next = newnode
    else:
        lst.head = newnode

def length(lst):
    """Return the length of a finite linked list"""
    count = 0
    current_node = lst.head
    while current_node is not None:
        count += 1
        current_node = current_node.next
    return count
def length(lst):
    count = 0
    current_node = lst.head
    while current_node is not None:
        count += 1
        current_node = current_node.next
    return count


def llprint(lst):
    current_node = lst.head
    while current_node:
        print(current_node.val, end=' ')
        current_node = current_node.next
    print() 


if __name__ == "__main__":
    linked_list = LList()

    for value in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]:
        append(linked_list, Node(value))

from genfinite import lst
print(length(lst))
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            n = self.head
            while n.next:
                n = n.next
            n.next = node

    def print_list(self):
        n = self.head
        while n:
            print(n.data, end=" --> ")
            n = n.next
        print("None")

    def sort(self):
        n = self.head
        while n:
            min_node = n
            next_node = n.next
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
            if min_node != n:
                n.data, min_node.data = min_node.data, n.data
            n = n.next


ll = LinkedList()
for i in reversed(range(10)):
    ll.append(i)
ll.print_list()
ll.sort()
ll.print_list()

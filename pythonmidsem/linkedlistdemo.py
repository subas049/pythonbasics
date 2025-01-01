# creating a linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_LL(self):
        if self.head is None:
            print("Linkedlist is Empty!!!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.next

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("The linked list is not Empty!!")

    def add_beign(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("node is not present in this list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            self.add_beign(data)
            return
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n is None:
                print("node is not present in this list")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            tv = self.head
            self.head = self.head.next
            tv.next = None

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None

    def del_after(self, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("node is not present in this list")
        else:
            n.next = n.next.next

    def del_before(self,x):
        if not self.head or not self.head.next or self.head.data==x:
            print("No node exist before the target value")
            return
        prev=None
        curr=self.head
        n=curr.next

        while n is not None:
            if n.data ==x:
                break
            prev=curr
            curr=n
            n=n.next
        if curr==self.head:
            self.head=n
        elif n is None:
            print("The value is not present in the list")
        else:
            prev.next=n


LL1 = LinkedList()
LL1.insert_empty(9999)
LL1.print_LL()
print("\n")
for i in reversed(range(5)):
    LL1.add_beign(i)
for i in range(5, 11):
    LL1.add_end(i)
LL1.print_LL()
print("\n")
LL1.add_after(99, 6)
LL1.add_before(99, 6)
LL1.print_LL()
print("\n")
LL1.delete_begin()
LL1.delete_end()
LL1.del_after(4)
LL1.print_LL()
LL1.del_before(2)
print("\n")
LL1.print_LL()

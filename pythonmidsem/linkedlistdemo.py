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
            print("\nLinkedlist is Empty!!!")
        else:
            n = self.head
            while n is not None:
                print(+n.data, end=" ")
                n = n.next
            print("\n")

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("\nThe linked list is not Empty!!")

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
            print("\nNode is not present in this list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("\nLinked list is empty")
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
                print("\nNode is not present in this list")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("\nLinked list is empty")
        else:
            tv = self.head
            self.head = self.head.next
            tv.next = None

    def delete_end(self):
        if self.head is None:
            print("\nLinked list is empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def del_after(self, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.next
        if n is None:
            print("\nNode is not present in this list")
        else:
            n.next = n.next.next

    def del_before(self, x):
        if not self.head or not self.head.next or self.head.data == x:
            print("\nNo node exist before the target value")
            return
        prev = None
        curr = self.head
        n = curr.next

        while n is not None:
            if n.data == x:
                break
            prev = curr
            curr = n
            n = n.next
        if curr == self.head:
            self.head = n
        elif n is None:
            print("\nThe value is not present in the list")
        else:
            prev.next = n

    def insert_atindex(self, data, index):
        if index == 0:
            self.add_beign(data)
        else:
            pos = 0
            n = self.head
            while n is not None:
                if pos == index - 1:
                    new_node = Node(data)
                    new_node.next = n.next
                    n.next = new_node
                    return
                n = n.next
                pos += 1
            if pos == index:
                new_node = Node(data)
                n = new_node
            else:
                print("\nThe index you have entered is larger than the length of the list")

    def del_atindex(self, index):
        if index == 0:
            self.delete_begin()
        else:
            pos = 0
            n = self.head
            while n.next is not None:
                if pos == index - 1:
                    n.next = n.next.next
                    return
                n = n.next
                pos += 1
            if pos == index:
                self.delete_end()
            else:
                print("\nThe index you have entered is larger than the length of the list")

    def len(self):
        count=0
        n=self.head
        while n:
            count+=1
            n=n.next
        return count



LL1 = LinkedList()
LL1.insert_empty(9999)
LL1.print_LL()
for i in reversed(range(5)):
    LL1.add_beign(i)
for i in range(5, 11):
    LL1.add_end(i)
LL1.print_LL()
LL1.add_after(99, 6)
LL1.add_before(99, 6)
LL1.print_LL()
LL1.delete_begin()
LL1.delete_end()
LL1.del_after(4)
LL1.print_LL()
LL1.del_before(2)
LL1.print_LL()
LL1.insert_atindex(8888, 3)
LL1.print_LL()
#LL1.insert_atindex(8888, 12)
LL1.insert_atindex(7777, 11)
LL1.insert_atindex(6666, 0)
LL1.insert_atindex(5555, 1)
LL1.print_LL()
LL1.del_atindex(13)
LL1.del_atindex(1)
LL1.del_atindex(4)
LL1.del_atindex(0)
LL1.print_LL()
print("The length of the linked list is : ", LL1.len())

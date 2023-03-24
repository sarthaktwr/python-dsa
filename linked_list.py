from logging import PercentStyle


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_value):
        node = Node(new_value)
        node.next = self.head
        self.head = node

    def insert(self, prev_value, new_value):
        node = Node(new_value)
        node.next = prev_value.next
        prev_value.next = node

    def append(self, new_value):
        node = Node(new_value)
        if self.head == None:
            self.head = node
            return
        last = self.head
        while(last.next):
            last = last.next
        last = node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        l = self.head
        while(l):
            print(l.data)
            l = l.next

    def dellist(self):
        curr = self.head
        while curr:
            prev = curr.next
            del curr.data
            curr = prev
    
    def count(self, node):
        if node is None:
            return 0
        return (1 + self.count(node.next))
    
    def getcount(self):
        return self.count(self.head)

    def reverselist(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(4)
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.insert(llist.head.next, 3)
    llist.reverselist()
    llist.getcount()
    llist.printList()
    # llist.dellist()
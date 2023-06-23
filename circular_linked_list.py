class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        """
        Adds a new node with the given data to the beginning of the linked list.
        
        :param data: the data to be stored in the new node
        :type data: any
        
        :return: None
        """
        if self.head is None:
            self.head = Node(data)
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        """
        Removes and returns the first element from the linked list.
        
        :return: The data of the removed node.
        """
        if self.head is None:
            return None
        
        self.head = self.head.next
    
        return self.head.data
    
    def print_list(self):
        """
        Prints all elements present in the linked list.
        
        Parameters:
        - self: The LinkedList object.
        
        Returns:
        - None
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.push(1)
    cll.push(2)
    cll.push(3)
    cll.push(4)
    cll.print_list()
    cll.pop()
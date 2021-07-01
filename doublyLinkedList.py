from typing import Iterator


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def  __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        
        if self.head is None: # LinkedList is empty
            self.head = new_node
            self.tail = new_node
        else: # LinkedList is not empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self,index):
        iterator = self.head 

        for _ in range(index):
            iterator = iterator.next   

        return iterator

    def find_node_with_data(self,data):
        iterator = self.head 

        while iterator is not None:
                if iterator.data == data:
                    return iterator
                
                iterator = iterator.next
        return None

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if previous_node == self.tail:
            new_node.prev = previous_node
            previous_node.next = new_node
            self.tail = new_node
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next

            previous_node.next.prev = new_node
            previous_node.next = new_node

            
    def __str__(self):
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next

        return res_str

# Empty LinkedList 
my_list = LinkedList()

# Append
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)


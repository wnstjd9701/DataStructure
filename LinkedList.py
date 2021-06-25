# Linked List Node Class
class Node:
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def find_node_at(self, index):
        iterator = self.head
        
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        new_node = Node(data)

        # LinkedList is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # LinkedList is not empty
        else: 
            self.tail.next = new_node
            self.tail = new_node

# Make new LinkedList
my_list = LinkedList()

# Append data at LinkedList
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

# Fine Node
# 데이터 가지고 오기
print("Find Node",my_list.find_node_at(3).data)

# 노드에 접근( 데이터 변경 )
my_list.find_node_at(0).data = 13

# Print LinkedList
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
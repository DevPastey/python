
# def two_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
            
# print(two_sum([2, 7, 11, 15]
# , 9))




# Linked List Node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class linked_list:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1
        
    def __str__(self):
        temp = self.head
        output = ""
        while temp is not None:
            output += f"{temp.value} -> "
            temp = temp.next
        return output + "None" 
        
my_linked_list = linked_list(1);
print(my_linked_list)
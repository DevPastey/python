# all_students = ["Mike", "John", "Sarah", "Emily", "David", "Jessica", "Daniel", "Laura", "James", "Olivia"]

# def find_student(name):
#     if name in all_students:
#         return f"Student {name} found in the database."
#     else:
#         return "Student not found!"
    
# print(find_student("Mikky"))





class MyArray:
    def __init__(self):
        self.data = []
        self.length = 0
        
    def push(self, value):
        self.data.append(value)
        self.length += 1
        return
        
    def get(self, index):
        return self.data[index]
    
    def pop(self):
        self.length -= 1
        popped = self.data[-1]
        self.data = self.data[:(self.length)]
        return popped
   
    def shift(self):
        self.length -= 1
        self.data = self.data[1:]
        return self.data
        
    def __str__(self):
        return f"My Array: length: {self.length}, data: {self.data} "
    
    
new_array = MyArray()
new_array.push("orange") 
new_array.push("apple")
new_array.push("banana")
new_array.push("watermelon")


print(new_array)
# print(new_array.get(3))
# print(new_array.get(1))
print(new_array.shift())
print(new_array)
print(new_array.get(1))



# print()
    
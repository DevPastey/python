# all_students = ["Mike", "John", "Sarah", "Emily", "David", "Jessica", "Daniel", "Laura", "James", "Olivia"]

# def find_student(name):
#     if name in all_students:
#         return f"Student {name} found in the database."
#     else:
#         return "Student not found!"
    
# print(find_student("Mikky"))





# class MyArray:
    # def __init__(self):
    #     self.data = []
    #     self.length = 0
        
    # def push(self, value):
    #     self.data.append(value)
    #     self.length += 1
    #     return
        
    # def get(self, index):
    #     return self.data[index]
    
    # def pop(self):
    #     self.length -= 1
    #     popped = self.data[-1]
    #     self.data = self.data[:(self.length)]
    #     return popped
   
    # def shift(self):
    #     self.length -= 1
    #     self.data = self.data[1:]
    #     return 
    
    # def delete(self, index):
    #     self.length -= 1
    #     self.data = [data for data in self.data if data != self.data[index]]
    #     return 
        
    # def __str__(self):
    #     return f"My Array: length: {self.length}, data: {self.data} "
    
    
# new_array = MyArray()
# new_array.push("orange") 
# new_array.push("apple")
# new_array.push("banana")
# new_array.push("watermelon")


# print(new_array)
# print(new_array.get(3))
# print(new_array.get(1))
# print(new_array.shift())
# print(new_array.delete(0))
# print(new_array)
# print(new_array.get(1))




# s1 = "Helllo"
# s2= "Apple"


# print("".join(reversed(s1)))



# string_1 = "abba"
# string_2 = "level"
# string_3 = "hello"



# def isPalidrome(string):
#         reversed_string = "".join(reversed(string))
#         if string == reversed_string:
#             return f"{string} is a palindrome"
#         else:
#             return f"{string} is not a palindrome"

# print(isPalidrome(string_1))
# print(isPalidrome(string_2))
# print(isPalidrome(string_3))


# def int_reverse(num):
#     return int(str(num)[::-1])

# print(int_reverse(1234))
# print(int_reverse(5678))



# text1 = "hello world"
# text2 = "huxn webdev"

# def capitalize(text):
    
#     sol = " ".join([x.capitalize() for x in text.split()])
#     return sol
    
        
# print(capitalize(text1))
# print(capitalize(text2 ))


# def fizz_buzz(num):
#     for i in range(1, num + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# print(fizz_buzz(15))

# arr = [7, 1, 5, 3, 6, 4] 

# min_val = min(arr)
# max_val = max(arr)
# max_profit = max_val - min_val
# print(max_profit) 

def chunk(arr, size):
    return [arr[i: i+size] for i in range(0, len(arr), size)]

print(chunk([1, 2,3,4,5,6,7,8], 3))
all_students = ["Mike", "John", "Sarah", "Emily", "David", "Jessica", "Daniel", "Laura", "James", "Olivia"]

def find_student(name):
    if name in all_students:
        return f"Student {name} found in the database."
    else:
        return "Student not found!"
    
print(find_student("Mikky"))
Python Medium
#16

n = int(input("Enter number :"))
fact=1
for i in range(2, n + 1):
    fact = fact * i
print("factorial is",fact)
factorial is 720
# 17

class VowelCounter:
    def __init__(self):
        self.vowels = "aeiouAEIOU"

    def count_vowels(self, string):
        count = 0
        for char in string:
            if char in self.vowels:
                count += 1
        return count

# Create an instance of VowelCounter
vc = VowelCounter()

# Count the vowels in the given string
result = vc.count_vowels("Programming is fun")
print(result)
5
# 18

for i in range(10):
    if i == 5:
        break
    print(i)
0
1
2
3
4
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed without break")
0
1
2
3
4
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
1
3
5
7
9
# 19

with open('ABC.txt', 'r') as file:
    lines = file.readlines()
        return len(lines)

# Count the number of lines in data.txt
line_count = count_lines_in_file('data.txt')
print(f'The number of lines in data.txt: {line_count}')
  Cell In[6], line 5
    return len(lines)
    ^
IndentationError: unexpected indent
# 20

class Student:
    def __init__(self, name=None):
        self._name = name

    # Getter method
    def get_name(self):
        return self._name

    # Setter method
    def set_name(self, name):
        self._name = name

# Create an instance of Student
student = Student()

# Set the name to "Alice"
student.set_name("Alice")

# Retrieve the name
name = student.get_name()
print(name)
Alice
# 21

# List of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

# Sort the list by the 'age' key
sorted_people = sorted(people, key=lambda x: x['age'])

print(sorted_people)
[{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
# 22

# Single Inheritance: Person -> Student
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

# Multilevel Inheritance: Person -> Student -> StudentGraduation
class StudentGraduation(Student):
    def __init__(self, name, age, student_id, graduation_year):
        super().__init__(name, age, student_id)
        self.graduation_year = graduation_year

    def display(self):
        super().display()
        print(f"Graduation Year: {self.graduation_year}")

# Creating objects and displaying their attributes
person = Person("Alice", 45)
student = Student("Bob", 20, "S12345")
student_graduation = StudentGraduation("Charlie", 22, "S67890", 2024)

print("Person:")
person.display()
print("\nStudent:")
student.display()
print("\nStudentGraduation:")
student_graduation.display()
Person:
Name: Alice, Age: 45

Student:
Name: Bob, Age: 20
Student ID: S12345

StudentGraduation:
Name: Charlie, Age: 22
Student ID: S67890
Graduation Year: 2024
# 23

def print_third_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                print(lines[2].strip())  # Print the third line
            else:
                print("The file has fewer than three lines.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Call the function with the filename
print_third_line('example.txt')
The file example.txt does not exist.
# 24

class Car:
    # Class variable to keep track of the total number of cars
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    # Static method to check if a car model is valid
    @staticmethod
    def is_valid_car_model(model):
        # Let's assume valid car models are stored in a set for this example
        valid_models = {"Sedan", "SUV", "Coupe", "Hatchback"}
        return model in valid_models

    # Class method to get the total number of cars
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Create some Car instances
car1 = Car("Toyota", "Sedan")
car2 = Car("Honda", "Coupe")

# Use the static method to check if a model is valid
print(Car.is_valid_car_model("SUV"))  # Output: True
print(Car.is_valid_car_model("Truck"))  # Output: False

# Use the class method to get the total number of cars
print(Car.get_total_cars())  # Output: 2
True
False
2
# 25

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def is_adult(self):
        return self.age >= 18

# Example usage:
person1 = Person("Alice", 25)
person1.display_details()  # Output: Name: Alice, Age: 25
print(person1.is_adult())  # Output: True

person2 = Person("Bob", 16)
person2.display_details()  # Output: Name: Bob, Age: 16
print(person2.is_adult())  # Output: False
Name: Alice, Age: 25
True
Name: Bob, Age: 16
False
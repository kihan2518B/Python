# Practice 1
# # Create a circle class add methods to find area and circumferences
#
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def Area(self):
#         area = (self.radius ** 2)*3.14
#         return area
#
#     def Circumference(self):
#         circumference = (self.radius * 2)*3.14
#         return circumference
#
#
# circle1 = Circle(5)
# print(circle1.radius)
# print(circle1.Area())
# print(circle1.Circumference())


# Practice 2
# Create Class Employee with role,department,salary, also give showdetails method
#
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#
#     def ShowDetails(self):
#         print("Role: ",self.role)
#         print("Department:",self.department)
#         print("Salary: ",self.salary)


# E1 = Employee("accountant","finance","40000")
# E1.ShowDetails()
#
# Create Engineer class that inherits property of Employee also add atttr: name and age
# class Engineer(Employee):
#     def __init__(self,name,age,role,department,salary):
#         self.name = name
#         self.age = age
#         super().__init__(role,department,salary)
#
# Eng1 = Engineer("Kishan",18,"Developer","IT","80000")
# Eng1.ShowDetails()

# Create class Order which stores item and its price

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("Burger",50)
order2 = Order("Pizza",450)
print(order1 < order2)
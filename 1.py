name = "Alice"
age = 25
print (name,"\n",age)
    
#---------------------------
age = 18
if age >= 18:
    print("Adult")
else:
    print("Minor")
    
#---------------------------
for i in range(5):
    print(i)
print("*************************")
#----------------------------
count = 0
while count < 5:
    print(count)
    count += 1
#-----------------------------
def greet(name):
    print("Hello", name)
greet("Samar")
#-----------------------------
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
#------------------------------
person = {"name": "Alice", "age": 25}
print(person["name"])
#------------------------------
colors = ("red", "green", "blue")
print(colors[0])
#------------------------------
Unique_nums = {1, 2, 2, 3}
print(Unique_nums) 
#---------------------------
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")





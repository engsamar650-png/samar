
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Fail")

for i in range(1, 11):
    print(i)

total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

word = "Python"
for letter in word:
    print(letter)
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

password = ""
while password != "1234":
    password = input("Enter the password: ")

print("Access granted!")


while True:
    word = input("Type 'exit' to stop: ")
    if word.lower() == "exit":
        break
    print("You typed:", word)

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else: print("Zero")

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "123":
    print("Login successful!")
else:
    print("Invalid credentials")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)



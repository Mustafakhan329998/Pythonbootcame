# Q1. Store your name and print it
name = "Mustafa Khan"
print("Name:", name)

# Q2. Create age and height variables
age = 19
height = 5.8
print("Age:", age)
print("Height:", height)

# Q3. Store a number and print its data type
num = 25
print("Number:", num)
print("Data type:", type(num))

# Q4. Boolean variable
is_student = True
print("Is Student:", is_student)

# Q5. Take one number from user
number = int(input("Enter a number: "))
print("You entered:", number)

## ✅ **Part B – Operators & Conditional Statements**

# Q6. Sum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# Q7. Check which number is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("First number is greater")
else:
    print("Second number is greater or equal")

# Q8. Even or Odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q9. Pass or Fail
marks = int(input("Enter marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Q10. Compare with 10
x = int(input("Enter a number: "))
if x < 10:
    print("Less than 10")
elif x == 10:
    print("Equal to 10")
else:
    print("Greater than 10")

## ✅ **Mini Project – Positive or Negative Number**


number = int(input("Enter a number: "))

if number >= 0:
    print("Positive Number")
else:
    print("Negative Number")


print('Part A: Loops (Very Easy)')
# Q1. Print numbers from 1 to 10 using a for loop.
for i in range (1 , 11 ,1):
    print(i)

# Q2. Print even numbers from 2 to 20 using a for loop.
print('=========EVEN NUMBER==============')
for i in range(2,20,2):
    print(i)    

# Q3. Print all characters of the string "Python" using a loop.
print("=======Python string========")

for ch in "python":
    print(ch)

# Q4. Print numbers from 5 to 1 using a loop.
print('====Printing the numbers====')
number = 5
while number > 0:
    print(number)
    number-=1   

# Q5. Use a while loop to print numbers from 1 to 5.    
print("==== using loop to print  the number ====")

num = 1

while num <= 5:
    print(num)
    num+=1 
    
print("Part B: Functions (Very Easy)")

# Q6.Create a function that prints "Hello Python" when called.
print("===Hello function===")
def greet():
    print("Hello")

greet()
# Q7. Create a function that takes one number and prints it.
print("=== number function ===")
def print_num(num):
    print(num)

print_num(99)    

# Q8. Create a function that takes two numbers and prints their sum.
print("====Sum d=function====")

def two_num_sum(x,y):
    s= x + y
    print(s)

two_num_sum(4,3)

# Q9. Create a function that takes one number and checks whether it is even or odd.

print("=== Cheacked if number is Even or odd. ")

def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter number here: "))
check_even_odd(number)

# Q10. Create a function that prints numbers from 1 to 5 using a loop.

print("======== function of loop =======")
def print_numbers():
    for i in range(1,6,1):
        print(i)
print_numbers()     


print("Mini Project (Very Simple)")

def number_table(num):
    for i in range(1,11):
        print(num, "x", i, "=", num * i)
number = int(input("Enter the number here: "))
number_table(number)        

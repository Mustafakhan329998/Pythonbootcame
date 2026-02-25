# 1. Create a set of your favorite 5 fruits. Add one more fruit and remove one fruit from
# the set. Print the final set.
print("=====SET QUESTION ======")
fruits_set = {"Apple","Banana","Mango","Grapes","Orange"}
fruits_set.add("Pineapple") # add one fruite
fruits_set.remove("Banana")  # remove one fruite
print(f"final Fruits set {fruits_set}")

# 2. Write a program to find the union and intersection of the following sets:
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 | set2

intersection_set = set1 & set2

print("Union:", union_set)
print("Intersection:", intersection_set)

print("===== TUPLE QUESTION =====")

# 3. Create a tuple with 5 numbers. Print the first and last number.

number = (1,2,3,4,5)

print("First number : ", number[0])

print("last number: ", number[-1])

# 4. Given the tuple (10, 20, 30, 40, 50), write a program to find the sum of all elements.

numbers = (1,2,3,4,5)

total = sum(numbers)

print("total sum of tuple: ", total)

# 5. Try to change the second element of the tuple (1, 2, 3) to 5. Observe what happens
# and explain why.

my_tuple = (1,2,3)
# my_tuple[0] = 5   # This will cause error

# In python the tuple are Tuples are immutable, meaning their elements cannot be changed after creation.
# If you try to modify it, Python raises:
# TypeError: 'tuple' object does not support item assignment

print("====LIST QUESTION====")

cities = ["Swabi", "Peshawar", "Lahore", "Karachi", "Islamabad"]

cities.append("Multan")          # Add at end
cities.insert(1, "Quetta")       # Insert at second position

print("Updated Cities List:", cities)

# 7. Given the list [2, 4, 6, 8, 10], write a program to double each number and store it
# in the same list.

Given_list = [2,4,6,8,10]
for i in range (len(Given_list)):
    Given_list[i] = Given_list[i] *2

print("Double of the Given list: ",Given_list)

print("====Dictionary Questions====")
# Question 8
marks = {
    "Math": 85,
    "Physics": 78,
    "Chemistry": 90
}

print("Math Marks:", marks["Math"])

# Question 9
marks["Physics"] = 88          # Update
marks["English"] = 75          # Add new subject

print("Updated Dictionary:", marks)

# Question 10
for subject, score in marks.items():
    print(f"{subject}: {score}")

    # Meni projects 

print("====Student Result Manger====")
# Distionary to store subject-wise marks
maths_marks = float(input("Enter the Maths marks: "))

physics_marks = float(input("Enter the physics marks: "))

chemistry_marks = float(input("Enter the chemisty marks: "))

marks ={
    "Maths" : maths_marks,
    "Physics" : physics_marks,
    "Chemistry": chemistry_marks
}

total = 0
# Calculate total marks
for sudject in marks:
    total = total + marks[sudject]
# Calculate average
Average = total / (len(marks))
# Average grade base on average
if Average >= 80:
    Grade = 'A'
elif Average >= 60:
    Grade = 'B'
else:
    Grade = 'C'

   
print("\n Subject-wise Marks")
# Display individual subject marks
for subject in marks:
   print(f"{subject} : {marks[subject]}")
# Display Total , Average , Grade
print("\nTotal Marks: ",total)
print(f"Average Marks:{Average:.2f}")
print(f"Grade:{Grade}")   


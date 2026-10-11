
1. Write a Python function to find the maximum of three numbers.
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example
print(find_max(10, 25, 15))
25
def find_max(a, b, c):
    return max(a, b, c)

x = float(input("Enter the First Number: "))
y = float(input("Enter the Second Number: "))
z = float(input("Enter the Third Number: "))

print("Max of Three Number is:", find_max(x, y, z))
Max of Three Number is: 25.0
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)

Expected Output : 20

# Here’s how you can write a Python function to sum all numbers in a list/tuple

def sum_numbers(lst):
    return sum(lst)

# Example
print(sum_numbers((8, 2, 3, 0, 7)))
20
3. Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)

Expected Output : -336

# Define a function named 'multiply' that takes a list of numbers as input
def multiply(numbers):
    # Initialize a variable 'total' to store the multiplication result, starting at 1
    total = 1
    
    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Multiply the current element 'x' with the 'total'
        total *= x
    
    # Return the final multiplication result stored in the 'total' variable
    return total

# Print the result of calling the 'multiply' function with a tuple of numbers (8, 2, 3, -1, 7)
print(multiply((8, 2, 3, -1, 7))) 
-336
# By using math.prod()
import math

def multiply_numbers(lst):
    return math.prod(lst)

print(multiply_numbers((8, 2, 3, -1, 7)))
-336
4. Write a Python function to reverse a string.
Sample String : "1234abcd"

Expected Output : "dcba4321"

# Define a function named 'string_reverse' that takes a string 'str1' as input
def string_reverse(str1):
    # Initialize an empty string 'rstr1' to store the reversed string
    rstr1 = ''
    
    # Calculate the length of the input string 'str1'
    index = len(str1)
    
    # Execute a while loop until 'index' becomes 0
    while index > 0:
        # Concatenate the character at index - 1 of 'str1' to 'rstr1'
        rstr1 += str1[index - 1]
        
        # Decrement the 'index' by 1 for the next iteration
        index = index - 1
    
    # Return the reversed string stored in 'rstr1'
    return rstr1

# Print the result of calling the 'string_reverse' function with the input string '1234abcd'
print(string_reverse('1234abcd'))
dcba4321
5. Write a Python function to check whether a number falls within a given range.
# Define a function named 'test_range' that checks 
# if a number 'n' is within the range 3 to 8 (inclusive)

def test_range(n):
    # Check if 'n' is within the range from 3 to 8 (inclusive) using the 'in range()' statement
    if n in range(3, 9):
        # If 'n' is within the range, print that 'n' is within the given range
        print("%s is in the range" % str(n))
    else:
        # If 'n' is outside the range, print that the number is outside the given range
        print("The number is outside the given range.")

# Call the 'test_range' function with the argument 5
test_range(5)
5 is in the range
6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
Sample String : 'The quick Brown Fox'

Expected Output:-

No. of Upper case characters : 3
No. of Lower case Characters : 13
# Define a function named 'string_test' that counts the number of upper and lower case characters in a string 's'
def string_test(s):
    # Create a dictionary 'd' to store the count of upper and lower case characters
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
    # Iterate through each character 'c' in the string 's'
    for c in s:
        # Check if the character 'c' is in upper case
        if c.isupper():
            # If 'c' is upper case, increment the count of upper case characters in the dictionary
            d["UPPER_CASE"] += 1
        # Check if the character 'c' is in lower case
        elif c.islower():
            # If 'c' is lower case, increment the count of lower case characters in the dictionary
            d["LOWER_CASE"] += 1
        else:
            # If 'c' is neither upper nor lower case (e.g., punctuation, spaces), do nothing
            pass
    
    # Print the original string 's'
    print("Original String: ", s)
    
    # Print the count of upper case characters
    print("No. of Upper case characters: ", d["UPPER_CASE"])
    
    # Print the count of lower case characters
    print("No. of Lower case Characters: ", d["LOWER_CASE"])

# Call the 'string_test' function with the input string 'The quick Brown Fox'
string_test('The quick Brown Fox') 
Original String:  The quick Brown Fox
No. of Upper case characters:  3
No. of Lower case Characters:  13
7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]

Unique List : [1, 2, 3, 4, 5]

# Define a function named 'unique_list' that takes a list 'l' as input and returns a list of unique elements
def unique_list(l):
    # Create an empty list 'x' to store unique elements
    x = []
    
    # Iterate through each element 'a' in the input list 'l'
    for a in l:
        # Check if the element 'a' is not already present in the list 'x'
        if a not in x:
            # If 'a' is not in 'x', add it to the list 'x'
            x.append(a)
    
    # Return the list 'x' containing unique elements
    return x

# Print the result of calling the 'unique_list' function with a list containing duplicate elements
print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))  
[1, 2, 3, 4, 5]
8. Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
# Here’s a simple way to check whether a string is a palindrome
# Define a function named 'isPalindrome' that checks if a string is a palindrome
def isPalindrome(string):
    # Initialize left and right pointers to check characters from the start and end of the string
    left_pos = 0
    right_pos = len(string) - 1
    
    # Loop until the pointers meet or cross each other
    while right_pos >= left_pos:
        # Check if the characters at the left and right positions are not equal
        if not string[left_pos] == string[right_pos]:
            # If characters don't match, return False (not a palindrome)
            return False
        
        # Move the left pointer to the right and the right pointer to the left to continue checking
        left_pos += 1
        right_pos -= 1
    
    # If the loop finishes without returning False, the string is a palindrome, so return True
    return True

# Print the result of checking if the string 'aza' is a palindrome by calling the 'isPalindrome' function
print(isPalindrome('madam')) 
True
9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white

Expected Result : black-green-red-white-yellow

# Take user input and split it into a list based on the hyphen ("-") separator, creating a list named 'items'
items = [n for n in input().split('-')]

# Sort the elements in the 'items' list in lexicographical order (alphabetical and numerical sorting)
items.sort()

# Join the sorted elements in the 'items' list using the hyphen ("-") separator and print the resulting string
print('-'.join(items)) 
black-green-red-white
10. Write a Python program to detect the number of local variables declared in a function.
# Define a function named 'abc'
def abc():
    # Define and assign values to local variables 'x', 'y', and 'str1' inside the function 'abc'
    x = 1
    y = 2
    str1 = "w3resource"
    
    # Print the string "Python Exercises"
    print("Python Exercises")

# Access the number of local variables in the function 'abc' using the __code__.co_nlocals attribute
print(abc.__code__.co_nlocals) 
3
11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
Sample Output:- 25 48
# Define a lambda function 'r' that takes a single argument 'a' and returns 'a + 15'
r = lambda a: a + 15

# Print the result of calling the lambda function 'r' with argument 10
print(r(10))

# Reassign 'r' to a new lambda function that takes two arguments 'x' and 'y' and returns their product
r = lambda x, y: x * y

# Print the result of calling the updated lambda function 'r' with arguments 12 and 4
print(r(12, 4))
25
48
12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
# Define a function 'func_compute' that takes a parameter 'n' and returns a lambda function
# The returned lambda function multiplies its argument 'x' by 'n'
def func_compute(n):
    return lambda x: x * n

# Assign the result of calling func_compute with argument 2 to the variable 'result'
result = func_compute(2)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Double the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 3
result = func_compute(3)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Triple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 4
result = func_compute(4)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quadruple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 5
result = func_compute(5)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quintuple the number 15 =", result(15))
Double the number of 15 = 30
Triple the number of 15 = 45
Quadruple the number of 15 = 60
Quintuple the number 15 = 75
13. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:- [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

Sorting the List of Tuples:- [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

# Create a list of tuples named 'subject_marks', each tuple containing a subject and its corresponding marks
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Display the original list of tuples to the console
print("Original list of tuples:")
print(subject_marks)

# Sort the 'subject_marks' list of tuples based on the second element of each tuple (the marks),
# using a lambda function as the sorting key to extract the second element
subject_marks.sort(key=lambda x: x[1])

# Display the sorted list of tuples to the console
print("\nSorting the List of Tuples:")
print(subject_marks) 
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
14. Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries:- [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries:- [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# Create a list of dictionaries named 'models', each dictionary representing a mobile phone model with 'make', 'model', and 'color' keys
models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Display a message indicating that the following output will show the original list of dictionaries
print("Original list of dictionaries:")
print(models)

# Sort the list of dictionaries ('models') based on the value associated with the 'color' key in each dictionary
# Uses the 'sorted()' function with a lambda function as the sorting key to sort based on the 'color' value
sorted_models = sorted(models, key=lambda x: x['color'])

# Display a message indicating that the following output will show the sorted list of dictionaries
print("\nSorting the List of dictionaries:")
print(sorted_models) 
Original list of dictionaries:
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

Sorting the List of dictionaries:
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
15. Write a Python program to filter a list of integers using Lambda.
Original list of integers:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even numbers from the said list:- [2, 4, 6, 8, 10]

Odd numbers from the said list:- [1, 3, 5, 7, 9]

# Create a list of integers named 'nums'
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Display a message indicating that the following output will show the original list of integers
print("Original list of integers:")
print(nums)

# Display a message indicating that the following output will show even numbers from the list
print("\nEven numbers from the said list:")

# Use the 'filter()' function with a lambda function to filter even numbers from 'nums'
# Create a new list 'even_nums' containing only the even numbers from the original list
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

# Display a message indicating that the following output will show odd numbers from the list
print("\nOdd numbers from the said list:")

# Use the 'filter()' function with a lambda function to filter odd numbers from 'nums'
# Create a new list 'odd_nums' containing only the odd numbers from the original list
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums) 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Even numbers from the said list:
[2, 4, 6, 8, 10]

Odd numbers from the said list:
[1, 3, 5, 7, 9]
16. Write a Python program to square and cube every number in a given list of integers using Lambda.
Original list of integers:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square every number of the said list:- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Cube every number of the said list:- [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

# Create a list of integers named 'nums'
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Display a message indicating that the following output will show the original list of integers
print("Original list of integers:")
print(nums)

# Display a message indicating that the following output will show each number in the list squared
print("\nSquare every number of the said list:")

# Use the 'map()' function with a lambda function to square each number in the 'nums' list
# Create a new list 'square_nums' containing the squared values of the original list
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

# Display a message indicating that the following output will show each number in the list cubed
print("\nCube every number of the said list:")

# Use the 'map()' function with a lambda function to cube each number in the 'nums' list
# Create a new list 'cube_nums' containing the cubed values of the original list
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums) 
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square every number of the said list:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Cube every number of the said list:
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
18. Write a Python program to find if a given string starts with a given character using Lambda.
# Define a lambda function 'starts_with' that checks if a given string starts with 'P'
starts_with = lambda x: True if x.startswith('P') else False

# Check if the string 'Python' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Python'))

# Redefine the lambda function 'starts_with' (same as before) to check if a string starts with 'P'
# Check if the string 'Java' starts with 'P' using the 'starts_with' lambda function
# Print the result which will be 'True' if the string starts with 'P', otherwise 'False'
print(starts_with('Java')) 
True
False
19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:- [-1, 2, -3, 5, 7, 8, 9, -10]

Rearrange positive and negative numbers of the said array:- [2, 5, 7, 8, 9, -10, -3, -1]

# Define a list 'array_nums' containing both positive and negative integers
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]

# Display a message indicating that the following output will show the original array
print("Original arrays:")
print(array_nums)  # Print the contents of 'array_nums'

# Use the 'sorted()' function to rearrange the elements in 'array_nums' based on a custom key
# The 'key' parameter uses a lambda function to sort the elements:
#   - It places positive numbers before negative numbers and zeros, maintaining their original order
#   - Zeros are placed at the front (index 0) of the sorted list
result = sorted(array_nums, key=lambda i: 0 if i == 0 else -1 / i)

# Display the rearranged array where positive numbers come before negative numbers and zeros
print("\nRearrange positive and negative numbers of the said array:")
print(result)  # Print the rearranged 'result' array.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]

Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:- [1, 2, 3, 5, 7, 8, 9, 10]

Number of even numbers in the above array: 3

Number of odd numbers in the above array: 5

# Create a list 'array_nums' containing integers
array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

# Display a message indicating that the following output will show the original array
print("Original arrays:")
print(array_nums)  # Print the contents of 'array_nums'

# Use the 'filter()' function with lambda functions to filter and count the number of odd and even numbers
# Use 'filter()' with a lambda function to filter and count the number of odd numbers in 'array_nums'
odd_ctr = len(list(filter(lambda x: (x % 2 != 0), array_nums)))

# Use 'filter()' with a lambda function to filter and count the number of even numbers in 'array_nums'
even_ctr = len(list(filter(lambda x: (x % 2 == 0), array_nums)))

# Display the number of even and odd numbers in the original array
print("\nNumber of even numbers in the above array: ", even_ctr)
print("\nNumber of odd numbers in the above array: ", odd_ctr)
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]

Number of even numbers in the above array:  3

Number of odd numbers in the above array:  5
21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
Orginal list:- [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

Numbers of the above list divisible by nineteen or thirteen:- [19, 65, 57, 39, 152, 190]

# Create a list 'nums' containing integers
nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Display a message indicating that the following output will show the original list
print("Orginal list:")
print(nums)  # Print the contents of the 'nums' list

# Use the 'filter()' function with a lambda function to filter numbers divisible by 19 or 13
# Filter elements from 'nums' using the lambda function to keep numbers divisible by 19 or 13
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums))

# Display numbers from the original list that are divisible by 19 or 13
print("\nNumbers of the above list divisible by nineteen or thirteen:")
print(result)  # Print the filtered 'result' list 
Orginal list:
[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

Numbers of the above list divisible by nineteen or thirteen:
[19, 65, 57, 39, 152, 190]
22. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
# Define a function 'check_string' that takes a string 'str1' as input
def check_string(str1):
    # Define a list 'messg' containing lambda functions with string validation conditions
    messg = [
        lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
        lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
        lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
        lambda str1: len(str1) >= 7 or 'String length should be at least 8.',
    ]
    
    # Generate a list 'result' by evaluating each lambda function in 'messg' for the input string 'str1'
    result = [x for x in [i(str1) for i in messg] if x != True]
    
    # Check if 'result' list is empty (all validation conditions are met)
    if not result:
        # If 'result' is empty, append 'Valid string.' indicating the string passes all validations
        result.append('Valid string.')
    
    # Return the 'result' list containing validation messages or 'Valid string.' if the string is valid
    return result    

# Get user input for a string 's'
s = input("Input the string: ")

# Print the result of string validation by calling the 'check_string' function with input 's'
print(check_string(s)) 
['Valid string.']
 git add pythonassignment2.py
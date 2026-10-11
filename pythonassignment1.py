
1. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ra"]

list2 = ["y", "me", "s", "hul"]

list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]

result = []

# Find the length of the shorter list to avoid index errors
min_len = min(len(list1), len(list2))

# Add items index-wise from both lists
for i in range(min_len):
    result.append(list1[i] + list2[i])

# Append leftover items from list1 if it is longer
if len(list1) > min_len:
    result.extend(list1[min_len:])
# Append leftover items from list2 if it is longer
elif len(list2) > min_len:
    result.extend(list2[min_len:])

print(result)
['My', 'name', 'is', 'Rahul']
# If we want output separately in a list then,
list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]

result = []

# Pair elements index-wise
for a, b in zip(list1, list2):
    result.append([a, b])

print(result)
[['M', 'y'], ['na', 'me'], ['i', 's'], ['Ra', 'hul']]
2. Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
3. Suppose you are given a list of candy and another list of same size representing no of items of respective candy. i.e -
candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']

no_of_items = [10,20,34,74,32]

Write a program to show no. of items of each candy type.

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']

no_of_items = [10, 20, 34, 74, 32]

# Use a loop to iterate through the lists and
# print the number of items for each candy type
for candy, count in zip(candy_list, no_of_items):
    print(candy, ":", count)
Jelly Belly : 10
Kit Kat : 20
Double Bubble : 34
Milky Way : 74
Three Musketeers : 32
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing:-
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

# solution
list1[2][2].append(7000)
print(list1)
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
4. Running Sum on list, Write a program to print a list after performing running sum on it. i.e:-
list1 = [1,2,3,4,5,6]
Running sum means:-
1
1+2 = 3
1+2+3 = 6
1+2+3+4 = 10
1+2+3+4+5 = 15
1+2+3+4+5+6 = 21
list1 = [1, 2, 3, 4, 5, 6]

running_sum = []
total = 0

for num in list1:
    total += num
    running_sum.append(total)

print(running_sum)
[1, 3, 6, 10, 15, 21]
5. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself. i.e.-
Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

like wise for all other elememts. [2,4,6,10,1]-->[22,20,16,10,23]

Example:-
[2, 4, 6, 10, 1]

For 2 → 2 + 4 + 6 + 10 = 22
For 4 → 4 + 6 + 10 = 20
For 6 → 6 + 10 = 16
For 10 → 10 = 10
For 1 → 1 + 2 + 4 + 6 + 10 = 23
Output:-
[22, 20, 16, 10, 23]

# For each element:- Add itself + all elements greater than it (from the list)
list1 = [2, 4, 6, 10, 1]

result = []

for i in list1:
    total = 0
    for j in list1:
        if j >= i:  # include itself and greater elements
            total += j
    result.append(total)

print(result)
[22, 20, 16, 10, 23]
6. Find list of common unique items from two list. and show in increasing order
Input:-
num1 = [23,45,67,78,89,34]

num2 = [34,89,55,56,39,67]

Output:-
[34, 67, 89]

# Here we have to find:-
# 1) Common elements in both lists
# 2) Only unique values
# 3) Output in increasing order

num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

# Find common unique elements and sort them
result = sorted(set(num1) & set(num2))

print(result)
[34, 67, 89]
7. Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
Input:-
['1ac21', '23fg', '456', '098d','1','kls']

Output:-
['456', '23fg', '1ac21', '1', 'kls', '098d']

# Here we have to calculate this:-
# '456' → 4×5×6 = 120
# '23fg' → 2×3 = 6
# '1ac21' → 1×2×1 = 2
# 'kls' → no digit → 1
# '098d' → 0×9×8 = 0

def product_of_digits(s):
    product = 1
    has_digit = False

    for ch in s:
        if ch.isdigit():
            product *= int(ch)
            has_digit = True

    return product if has_digit else 1


data = ['1ac21', '23fg', '456', '098d', '1', 'kls']

# Sort based on product of digits (descending)
result = sorted(data, key=product_of_digits, reverse=True)

print(result)
['456', '23fg', '1ac21', '1', 'kls', '098d']
8. Write a program that can find the max number of each row of a matrix
Example:-
Input:-
[[1,2,3],[4,5,6],[7,8,9]]

Output:-
[3,6,9]

# Find the maximum number from each row of a matrix.

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = []

for row in matrix:
    result.append(max(row))

print(result)
[3, 6, 9]
# By using max():-
# max() -> works directly on lists, so it's very efficient

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = [max(row) for row in matrix]

print(result)
[3, 6, 9]
9. Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- - Primary Skill, - Higher Education, - Year of Graduation.
Show every students record in the form of tuples if matches all required criteria.

It is assumed that there will be only one primary skill.

If no such candidate found, print No such candidate.

Input:-
Enter No of records- 2

Enter Details of student-1

Enter Student name- Manohar

Enter Higher Education- B.Tech

Enter Primary Skill- Python

Enter Year of Graduation- 2022

Enter Details of student-2

Enter Student name- Ponian

Enter Higher Education- B.Sc.

Enter Primary Skill- C++

Enter Year of Graduation- 2020

Enter Job Role Requirement

Enter Skill- Python

Enter Higher Education- B.Tech

Enter Year of Graduation- 2022

Output:-
('Manohar', 'B.tech', 'Python', '2022')

# Input the number of records
num_records = int(input("Enter No of records: "))

# Initialize a list to store the student records
students = []

# Input the student details
for i in range(num_records):
    print(f"Enter Details of student-{i + 1}")
    name = input("Enter Student name: ")
    education = input("Enter Higher Education: ")
    skill = input("Enter Primary Skill: ")
    graduation_year = input("Enter Year of Graduation: ")

 # Store the student record as a tuple in the 'students' list
    students.append((name, education, skill, graduation_year))

# Input the job role requirements
print("\nEnter Job Role Requirement")
required_skill = input("Enter Skill: ")
required_education = input("Enter Higher Education: ")
required_year = input("Enter Year of Graduation: ")

# Shortlist candidates based on the job role requirements
shortlisted_candidates = []

for student in students:
    name, education, skill, graduation_year = student
    if skill == required_skill and education == required_education and graduation_year == required_year:
        shortlisted_candidates.append(student)

# Output the shortlisted candidates or "No such candidate"
if shortlisted_candidates:
    for candidate in shortlisted_candidates:
        print(candidate)
else:
    print("No such candidate")
Enter Details of student-1
Enter Details of student-2
Enter Job Role Requirement
('Manohar', 'B.Tech', 'Python', '2022')
10. Write a program to find set of common elements in three lists using sets.
# Input:-

ar1 = [1, 5, 10, 20, 40, 80]

ar2 = [6, 7, 20, 80, 100]

ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Output:- [80, 20]
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Find common elements using sets
result = list(set(ar1) & set(ar2) & set(ar3))

print(result)
[80, 20]
11. Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
Input:-
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
Output:-
No of unique vowels-6
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

# Define vowels (both lowercase and uppercase treated differently)
vowels = "aeiouAEIOU"

# Use set to store unique vowels
unique_vowels = set()

for ch in Str1:
    if ch in vowels:
        unique_vowels.add(ch)

# Count of unique vowels
print("No of unique vowels-", len(unique_vowels))
No of unique vowels- 6
12. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
Example 1:-
Input:-
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}

lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
Output:-
[9, 10, 4, 5]
Example 2:-
Input:-
lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}

lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
Output:-
[9, 11, 26, 28]
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

# Intersection using list comprehension
result = [x for x in lst1 if x in lst2]

print(result)
[4, 5, 9, 10]
13. Convert a list of Tuples into Dictionary.
Example 1:-
Input:-
[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
Output:-
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
Example 2:-
Input:-
[('A', 1), ('B', 2), ('C', 3)]
Output:-
{'A': [1], 'B': [2], 'C': [3]}
# Example:- 01
data = [("akash", 10), ("gaurav", 12), ("anand", 14), 
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]

result = {}

for key, value in data:
    result[key] = [value]

print(result)
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
# Example 02:-
data = [('A', 1), ('B', 2), ('C', 3)]

result = {}

for key, value in data:
    result[key] = [value]

print(result)
{'A': [1], 'B': [2], 'C': [3]}
# 14. Write a Python function that takes a list and returns a new list with unique elements of the first list.
Exercise 1:-
Input:-
[1,2,3,3,3,3,4,5]
Output:-
[1, 2, 3, 4, 5]
# Here we need a function that removes duplicates and returns only unique elements.

def unique_list(lst):
    return list(set(lst))

# Example
print(unique_list([1,2,3,3,3,3,4,5]))
[1, 2, 3, 4, 5]
# If you want to keep original order (important) then
def unique_list(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

# Example
print(unique_list([1,2,3,3,3,3,4,5]))
[1, 2, 3, 4, 5]
15. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
# You need to print only even numbers from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = []

for i in lst:
    if i % 2 == 0:
        even_numbers.append(i)

print(even_numbers)
[2, 4, 6, 8]
# By Using List Comprehension:- 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = [i for i in lst if i % 2 == 0]

print(even_numbers)
[2, 4, 6, 8]
16. Write a Python function to check whether a number is perfect or not. A Perfect number is a number that is half the sum of all of its positive divisors (including itself).
Example:-
The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.

Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.

The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

# You need to check whether a number is a perfect number
def is_perfect(n):
    total = 0
    
    # Find sum of proper divisors
    for i in range(1, n):
        if n % i == 0:
            total += i
    
    # Check condition
    if total == n:
        return True
    else:
        return False

# Example
num = int(input("Enter a number: "))

if is_perfect(num):
    print(num, "is a Perfect Number")
else:
    print(num, "is NOT a Perfect Number")
6 is a Perfect Number
17. Write a Python function to concatenate any no of dictionaries to create a new one.
Sample Dictionary:-
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# You need a function to concatenate (merge) any number of dictionaries.

def merge_dicts(*dicts):
    result = {}
    
    for d in dicts:
        result.update(d)
    
    return result

# Example
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print(merge_dicts(dic1, dic2, dic3))
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
18. Write a python function that receives a list of integers and prints out a histogram of bin size 10
Input:-
[13,42,15,37,22,39,41,50]
Output:-
{11-20:2,21-30:1,31-40:2,41-50:3}
# You need to group numbers into bins of size 10 and count how many fall in each range
def histogram(lst):
    result = {}
    
    for num in lst:
        # Find bin range
        start = (num // 10) * 10 + 1
        end = start + 9
        
        key = f"{start}-{end}"
        
        # Count frequency
        result[key] = result.get(key, 0) + 1
    
    return result

# Example
data = [13,42,15,37,22,39,41,50]
print(histogram(data))
{'11-20': 2, '41-50': 2, '31-40': 2, '21-30': 1, '51-60': 1}
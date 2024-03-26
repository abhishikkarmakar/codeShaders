import streamlit as st

# Define tasks for each mode
modes_tasks = {
    "Flow of Program": [
        "Input a year and find whether it is a leap year or not.",
        "Take two numbers and print the sum of both.",
        "Take a number as input and print the multiplication table for it.",
        "Take 2 numbers as inputs and find their HCF and LCM.",
        "Keep taking numbers as inputs till the user enters 'x', after that print sum of all.",
    ],
    "First Java": [
        "Write a program to print whether a number is even or odd, also take input from the user.",
        "Take name as input and print a greeting message for that particular name.",
        "Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.",
        "Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)",
        "Take 2 numbers as input and print the largest number.",
        "Input currency in rupees and output in USD.",
        "To calculate Fibonacci Series up to n numbers.",
        "To find out whether the given String is Palindrome or not.",
        "To find Armstrong Number between two given number.",
    ],
    "Conditionals and Loops": [
        "Basic Java Programs",
        "Area Of Circle Java Program",
        "Area Of Triangle",
        "Area Of Rectangle Program",
        "Area Of Isosceles Triangle",
        "Area Of Parallelogram",
        "Area Of Rhombus",
        "Area Of Equilateral Triangle",
        "Perimeter Of Circle",
        "Perimeter Of Equilateral Triangle",
        "Perimeter Of Parallelogram",
        "Perimeter Of Rectangle",
        "Perimeter Of Square",
        "Perimeter Of Rhombus",
        "Volume Of Cone Java Program",
        "Volume Of Prism",
        "Volume Of Cylinder",
        "Volume Of Sphere",
        "Volume Of Pyramid",
        "Curved Surface Area Of Cylinder",
        "Total Surface Area Of Cube",
        "Fibonacci Series In Java Programs",
        "Subtract the Product and Sum of Digits of an Integer",
        "Input a number and print all the factors of that number (use loops).",
        "Take integer inputs till the user enters 0 and print the sum of all numbers (HINT: while loop)",
        "Take integer inputs till the user enters 0 and print the largest number from all.",
        "Addition Of Two Numbers",
        "Intermediate Java Programs",
        "Factorial Program In Java",
        "Calculate Electricity Bill",
        "Calculate Average Of N Numbers",
        "Calculate Discount Of Product",
        "Calculate Distance Between Two Points",
        "Calculate Commission Percentage",
        "Power In Java",
        "Calculate Depreciation of Value",
        "Calculate Batting Average",
        "Calculate CGPA Java Program",
        "Compound Interest Java Program",
        "Calculate Average Marks",
        "Sum Of N Numbers",
        "Armstrong Number In Java",
        "Find Ncr & Npr",
        "Reverse A String In Java",
        "Find if a number is palindrome or not",
        "Future Investment Value",
        "HCF Of Two Numbers Program",
        "LCM Of Two Numbers",
        "Java Program Vowel Or Consonant",
        "Perfect Number In Java",
        "Check Leap Year Or Not",
        "Sum Of A Digits Of Number",
        "Kunal is allowed to go out with his friends only on the even days of a given month. Write a program to count the number of days he can go out in the month of August.",
        "Write a program to print the sum of negative numbers, sum of positive even numbers and the sum of positive odd numbers from a list of numbers (N) entered by the user. The list terminates when the user enters a zero.",
    ],
    "Functions": [
        "Define two methods to print the maximum and the minimum number respectively among three numbers entered by the user.",
        "Define a program to find out whether a given number is even or odd.",
        "A person is eligible to vote if his/her age is greater than or equal to 18. Define a method to find out if he/she is eligible to vote.",
        "Write a program to print the sum of two numbers entered by user by defining your own method.",
        "Define a method that returns the product of two numbers entered by user.",
        "Write a program to print the circumference and area of a circle of radius entered by user by defining your own method.",
        "Define a method to find out if a number is prime or not.",
        "Write a program that will ask the user to enter his/her marks (out of 100). Define a method that will display grades according to the marks entered.",
        "Write a program to print the factorial of a number by defining a method named 'Factorial'.",
        "Write a function to find if a number is a palindrome or not. Take number as parameter.",
        "Convert the programs in flow of program, first java, conditionals & loops assignments into functions.",
        "Write a function to check if a given triplet is a Pythagorean triplet or not.",
        "Write a function that returns all prime numbers between two given numbers.",
        "Write a function that returns the sum of first n natural numbers.",
    ],
    "Arrays": [
        "Build Array from Permutation",
        "Concatenation of Array",
        "Running Sum of 1d Array",
        "Richest Customer Wealth",
        "Shuffle the Array",
        "Kids With the Greatest Number of Candies",
        "Number of Good Pairs",
        "How Many Numbers Are Smaller Than the Current Number",
        "Cells with Odd Values in a Matrix",
        "Find the Highest Altitude",
        "Sum of All Subset XOR Totals",
        "Count Items Matching a Rule",
        "Find the Winner of the Circular Game",
        "Maximum Population Year",
    ],
    "Searching": [
        "Binary Search",
        "Linear Search",
        "Jump Search",
        "Interpolation Search",
        "Exponential Search",
        "Fibonacci Search",
        "Ternary Search",
        "Kth Smallest/Largest Element in Unsorted Array",
    ],
    "Sorting": [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Heap Sort",
        "Quick Sort",
        "Counting Sort",
        "Radix Sort",
        "Bucket Sort",
    ],
    "Strings": [
        "Reverse a String",
        "Reverse Words in a String",
        "Valid Palindrome",
        "Check if a string is a rotation of another string",
        "Reverse Vowels in a String",
        "Check if a string is a Pangram or not",
        "Check if two strings are Anagram or not",
        "Implement strstr()",
        "Longest Substring Without Repeating Characters",
        "Minimum Window Substring",
        "Longest Palindromic Substring",
        "Regular Expression Matching",
        "String to Integer (atoi)",
        "Implement strStr()",
        "Count and Say",
        "Longest Common Prefix",
        "Group Anagrams",
        "Valid Parentheses",
        "Valid Palindrome II",
        "Roman to Integer",
        "Integer to Roman",
    ],
    "Patterns": ["Print the following pattern for n number of rows:"],
    "Recursion": [
        "Factorial of a Number",
        "Fibonacci Series",
        "Sum of Digits of a Number",
        "Power of a Number",
        "Tower of Hanoi",
        "GCD of Two Numbers",
        "Product of Two Numbers",
        "Print n to 1",
        "Print 1 to n",
    ],
    "Bitwise": [],  # No problems provided
    "Math": [],  # No problems provided
    "Complexities": [],  # No problems provided
    "Object Oriented Programming": [],  # No problems provided
    "Linked List": [],  # No problems provided
    "Stacks and Queues": [],  # No problems provided
    "Trees": [],  # No problems provided
    "Heaps": [],  # No problems provided
}


# Function to initialize or load session state
def init_session_state():
    return {
        "checkboxes": {mode: {} for mode in modes_tasks},
        "comments": {mode: {} for mode in modes_tasks},
    }


# Initialize or load session state
def get_session_state():
    if "state" not in st.session_state:
        st.session_state.state = init_session_state()
    return st.session_state.state


# Sidebar - Mode selection
selected_mode = st.sidebar.selectbox("Select Mode", list(modes_tasks.keys()))

# Display tasks for selected mode
st.title(selected_mode)
tasks = modes_tasks[selected_mode]

# Get the checkboxes and comments for the selected mode
state = get_session_state()
checkboxes = state["checkboxes"][selected_mode]
comments = state["comments"][selected_mode]

for task in tasks:
    checkbox = st.checkbox(task, value=checkboxes.get(task, False))
    checkboxes[task] = checkbox

    comment = st.text_input(f"Comments for {task}", value=comments.get(task, ""))
    comments[task] = comment

# Save checkboxes and comments back to session state
state["checkboxes"][selected_mode] = checkboxes
state["comments"][selected_mode] = comments

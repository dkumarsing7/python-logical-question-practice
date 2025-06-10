# Task: Get all squares of even numbers between 1 and 20, but skip 10
task1 = [x**2 for x in range(1,20) if x%2==0 and x!=10]
print(task1)

# List of vowels from a string.
task2 = "Hello World"
task2 = [char for char in task2 if char in ['a','e','i','o','u','A','E','I','O','U'] ]
print(task2)

# List of words longer than 4 letters from a sentence.
sentence = "This is a simple sentence with some long words"
tokenized_sentence = sentence.split()
task3 = [four_letter for four_letter in tokenized_sentence if len(four_letter)==4 ]
print(task3)

# Flatten a 2D list using nested list comprehension.
TwoD = [[input() for i in range(3)]for j in range(2)]
print(TwoD)

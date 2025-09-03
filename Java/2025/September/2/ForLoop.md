```
1. A for loop is a programming construct used to iterate over a sequence of items, such as a list, string, or range of numbers. It's one of the fundamental control flow statements that allows you to execute a block of code repeatedly for each item in the sequence.

How It Works
Initialization: The loop starts by taking the first item from the sequence.

Execution: The block of code inside the loop is executed with the current item.

Iteration: The loop then moves to the next item in the sequence.

Repetition: Steps 2 and 3 are repeated until all items in the sequence have been processed.

Basic Syntax (Python Example)
Python

# A simple list of fruits
fruits = ["apple", "banana", "cherry"]

# Loop through each fruit in the list
for fruit in fruits:
  print(fruit)
Key Concepts
Iterable: An object that can be iterated over (e.g., a list, tuple, dictionary, or string).

Iteration Variable: A temporary variable (like fruit in the example) that holds the value of the current item during each pass of the loop.

Loop Body: The code block that gets executed on each iteration.

Why Use a for Loop?
for loops are ideal for situations where you know the number of iterations in advance or when you need to perform an action for every item in a collection.

Efficiency: They provide a concise and readable way to handle repetitive tasks.

Readability: The syntax is often more intuitive than other looping structures, making the code easier to understand.

Common Applications:

Processing items in a list.

Iterating through characters in a string.

Repeating a task a specific number of times.
```
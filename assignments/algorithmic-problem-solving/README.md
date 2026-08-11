# 📘 Assignment: Algorithmic Problem Solving

## 🎯 Objective

Practice list and dictionary algorithms in Python by building functions that analyze data, filter results, and solve a step-by-step problem using loops and conditionals.

## 📝 Tasks

### 🛠️ Analyze number data

#### Description
Write a function that examines a list of numbers and returns a summary of the dataset.

#### Requirements
Completed program should:

- Define `summarize_numbers(numbers)` that returns a dictionary with `count`, `sum`, `average`, `min`, and `max`
- Use a loop to compute values instead of built-in summary functions
- Return the summary dictionary
- Example:
  ```python
  print(summarize_numbers([2, 5, 8]))
  # {'count': 3, 'sum': 15, 'average': 5.0, 'min': 2, 'max': 8}
  ```

### 🛠️ Filter and search with dictionaries

#### Description
Work with a list of student records to find only the students whose grade meets a minimum threshold.

#### Requirements
Completed program should:

- Define `filter_students_by_grade(students, threshold)` where `students` is a list of dictionaries with `name` and `grade`
- Return a list of student names whose grade is greater than or equal to `threshold`
- Use loop and conditional logic to decide which students pass
- Example:
  ```python
  students = [
      {'name': 'Ava', 'grade': 84},
      {'name': 'Ben', 'grade': 76},
      {'name': 'Mia', 'grade': 91}
  ]
  print(filter_students_by_grade(students, 80))
  # ['Ava', 'Mia']
  ```

### 🛠️ Solve a step-by-step algorithm challenge

#### Description
Build a function that finds all prime numbers below a given limit using nested loops.

#### Requirements
Completed program should:

- Define `find_primes(limit)` that returns a list of prime numbers less than `limit`
- Use loops and conditionals to check each number for primality
- Do not use any external math libraries for prime checking
- Example:
  ```python
  print(find_primes(10))
  # [2, 3, 5, 7]
  ```

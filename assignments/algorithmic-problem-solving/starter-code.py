def summarize_numbers(numbers):
    """Return a summary dictionary for the list of numbers."""
    # Use a loop to compute count, sum, min, and max.
    pass


def filter_students_by_grade(students, threshold):
    """Return names of students whose grade is >= threshold."""
    # Use a loop and conditional logic.
    pass


def find_primes(limit):
    """Return a list of prime numbers less than the given limit."""
    # Use nested loops to test each candidate number.
    pass


if __name__ == "__main__":
    print(summarize_numbers([2, 5, 8]))
    print(filter_students_by_grade([
        {'name': 'Ava', 'grade': 84},
        {'name': 'Ben', 'grade': 76},
        {'name': 'Mia', 'grade': 91}
    ], 80))
    print(find_primes(10))

def sum_even_numbers(numbers):
    """
    Calculates the sum of all even numbers in the given list of integers.

    Args:
    numbers: list of integers

    Returns:
    sum of all even numbers in the list
    """

    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers(numbers)
print(even_sum)  # Output: 30

numbers_2 = [1, 65, 34, 92, 184, 5, 7, 21, 306, 66, 19]
even_sum = sum_even_numbers(numbers_2)
print(even_sum)

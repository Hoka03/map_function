"""
Create map function
"""

def map_solution(func, iterable):
    for item in iterable:
        yield func(item)

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x + x

square_list = map_solution(square, numbers)
print(list(square_list))

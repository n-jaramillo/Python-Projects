# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
    return max(x, y, z)

print(max_num(1, 6, 4))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) != 0:
        result = 1
        for i in lst:
            result *= i
        return result
    else:
        return 0

print(mult_list([1, 6, 4, 7]))
print(mult_list([]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

print(rev_string("Hello World"))

# Write a Python function called num_within() to check whether a number falls in a given range.
    # The function accepts the number, beginning of range, and end of range(inclusive) as arguments.
    # Examples: num_within(3, 2, 4) returns True, num_within(3, 1, 3) returns True, num_within(10, 2, 5) returns False.
def num_within(n, range_start, range_end):
    return n in range(range_start, range_end+1)

print(num_within(3, 1, 3))
print(num_within(3, 2, 4))
print(num_within(10, 2, 5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
    # The function accepts the number n, the number of rows to print
    # Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    # nCr, binomial coefficient to get Pascal triangle
    for i in range(1, n + 1):
        k = 1
        for j in range(1, i + 1):
            print(' ', k, sep='', end='')

            k = k * (i - j) // j
        print()

pascal(9)

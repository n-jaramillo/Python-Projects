def check_string(str, other):
	# if string contains other string return True
	if other in str:
		return True

	# else return False
	else:
		return False

def recursive_sum(num):
	# base case 
	# if num is equal to 0 return num
	if num == 0:
		return num

	# recursive case
	# else return sum of num and function starting at num - 1
	else:	
		return num + recursive_sum(num-1)

def reverse_string(str):
	# return a reversed slice of str
	return str[::-1]

def recursive_capitalize(lst):
	# base case 
	# if length of lst is 1 then return element capitalized
	if len(lst) == 1:
		return lst[0].upper()

	# recursive case
	# return formatted string of first element of lst capitalized with function starting lst at second element
	else:
		return f"{lst[0].upper()} {recursive_capitalize(lst[1:])}"

def find_product(lst):
	# set product equal to 1 (if equal to 0 the return would be 0 regardless of other numbers in lst)
	product = 1

	# for every element in lst set product equal to product multiplied by element
	for i in lst:
		product *= i

	# return product
	return product

def find_unique(lst):
    # return a lambda of lst to print only unique values, if count of element is equal to 1
	return [i for i in lst if lst.count(i) == 1]


# Test Code 
print(check_string("Hello World", "Hello"))
print(check_string("Hello World", "Bye"))

print(recursive_sum(5))
print(recursive_sum(8))

print(reverse_string("hello"))
print(reverse_string("Hello World"))

print(recursive_capitalize(['pandas', 'monkeys', 'koalas', 'kangaroos']))

print(find_product([4, 3, 5]))
print(find_product([7, 8, 9]))

print(find_unique([1, 5, 1, 6, 8, 5]))
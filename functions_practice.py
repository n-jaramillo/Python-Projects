# Function 1
# Prints greeting to user

def hello():
    print("Hello user")

# Function 2
# Returns a list with arguments as elements

def pack(a, b, c):
    return [a, b, c]

# Function 3
# Prints a series of strings based on list elements

def eat_lunch(in_list):
    if len(in_list) == 0:
        print("My lunchbox is empty!")

    else:
        print(f'First I eat {in_list[0]}')
        for i in in_list[1:]:
            print(f'Next I eat {i}')

# Testing
hello()
pack(1, 2, 3)
eat_lunch([])
eat_lunch(["steak and eggs", "tacos", "chicken alfredo pasta"])
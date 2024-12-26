# this is a function without args

def example():
    print("this is a sample no parameter and void function")


example()


# this is a function with args
def example(a, b):
    print(a + b)


example(12, 23)
example("Hi ", "Subash")


def example(firstname, lastname):
    print('Hi ' + firstname + ' ' + lastname)


example(firstname="subash", lastname="perumal")


# sum of n natural numbers

def sum(n):
    val = 0
    for i in range(n + 1):
        val = val + i
    return val


print(sum(5))

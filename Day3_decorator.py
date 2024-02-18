"""def shruti(func):
    def wrapper():
        print(func)
        print("Something is happpening before the function is being called")
        func()
        print("Something is happpening after the function is being called")
    return wrapper

print("Main Program begins")
@shruti
def say_hello():
    print("Hello")
say_hello()"""

def decorator(func):
    def wrapper(*args):
        print("we will now start the operation")
        print(func)
        result = func(*args)
        print("calculation completed result is {}".format(result))
    return wrapper

print("We start the main program", end="\n")

@decorator
def add(a,b):
    result = a+b
    return result
@decorator
def sub(a,b):
    result = a-b
    return result
add(10,20)
print()
sub(7,1)
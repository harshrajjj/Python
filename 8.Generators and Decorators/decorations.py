from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet();
print(greet.__name__)
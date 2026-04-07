from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@logging_decorator
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: Calling function 'add_numbers' with arguments: (3, 5) and keyword arguments: {}
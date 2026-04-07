from functools import wraps

def auth_decorator(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == 'admin':
            print("Access granted.")
        else:
            return func(user_role)
    return wrapper

@auth_decorator
def access_resource(user_role):
    print(f"Access denied for user role: {user_role}")

access_resource('admin')
access_resource('user')
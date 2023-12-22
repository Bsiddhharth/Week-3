# decorator that prepends a string to the return values of the function it decorates
def prepend_string_decorator(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return prefix + str(result)
        return wrapper
    return decorator

# Usage example
@prepend_string_decorator("Prefix: ")
def my_function(ff):
    return "Hello"

result = my_function()
print(result)  # Output will be "Prefix: Hello"
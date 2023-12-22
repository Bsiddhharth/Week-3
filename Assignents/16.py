def decorator_fn(func):
    def fn():
        print('HELLO WORLD')
        func()
    return fn    

@decorator_fn
def print_func():
    pass

print_func()
    
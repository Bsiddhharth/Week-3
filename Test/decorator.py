# def cool():
#     def super():
#         return '\t this is cool'
    
#     print(type(super))
#     return super


# func=cool()
# print(func())


# def hello():
#     print("hello")
    
# def other(some_func):
#     print("fn passed as arg")
#     print(some_func())
    
# other(hello)    
        
# def new_deco(a):
#     def wraps():
#         print("1st statemen")
#         a()
#         print("last statement")
        
#     return wraps

# # @new_deco
# def needs_decorator():
#   print("This fn needs decorator")   
  
  
# needs_decorator()  

# def sample_deco(func):
#   def wrapper(a,b):
#     if b==0:
#       print("Error")
#       return None
#     return func(a,b)
#   return wrapper

# @sample_deco
# def divv(a,b):
#   print(a/b)    
    
    
# divv(5,0)    
  
  
    
  

# list=[1,2,3,4,'a']
# print(list)

# list.append('l')
# print(list)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print(key,end='')
    
# print(my_dict.keys())
# print(my_dict.values())

# for x,y in my_dict.items():
#     print(x,end='')
#     print(y,end='')
    
# print(my_dict.get('a'))
# x=my_dict.keys()

# print(x)

# def simple_gen():
#     yield 1
#     yield 2
#     yield 3
    
    
# gen = simple_gen() 
# for value in gen:
#     print(value)
    
# import sys    
# l=[x for x in range(1,100000)]
# print(sys.getsizeof(l)) 


# gen = (x for x  in range(1,10000))
# print(sys.getsizeof(gen))

# gen = (range(10))

# gen1= (x for x in range(10))
# print(sys.getsizeof(gen1))



def deco(func):
    def wrapper(a,b):
        if b==0:
            print("EROOR")
            return None
        return func(a,b)
    return wrapper


@deco             
def div(a,b):
    print(a/b)

# div(3,0)

# class smaple:
#     def __init__(self,value):
#         self.value=value
        
#     def __str__(self):
#        return f"the stirng: {self.value}"  
        
# obj = smaple(42)

# print(obj)          

# a="  i am sidharth  "
# # b=[]
# # c=[]
# # for i in range(len(a)):
# #     if i%2==0:
# #         b.append(a[i].upper())
# #     else:
# #         b.append(a[i])

# # c="".join(b)   
# # print(c)        

        

# b=a.strip()
# print(a.split(" "))

# print(b.split(" "))
# lp=[1,2,3,'we','are']
# lp="adolf"
# mi=iter(lp)

# print(next(mi))
# print(next(mi)) 
# print(next(mi))
# print(next(mi))

# def evn_generate():
#     n=0
#     while True:
#        yield n
#        n+=2
    
# evn=evn_generate()

# for i in range(5):
#     print(next(evn))
        
        
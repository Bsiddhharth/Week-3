# x=range(6)

# print(x)

# for i in range(6):
#     print(i,end=' ')
    
    
# print()        
# v=5.4
# y=complex(v)            #coverting int or float to complex is possible
# print(y)    


# z=5+4j        #cant convert complex to another datatype
# c=float(z)
# print(c)    

# random number

# import random

# print(random.randrange(1,10))

# print(ord('A'))
# print(chr(65))

A=[2,3,4,5,6,7]

# evn=[]
# odd=[]

# for i in A:
#     if i%2==0:
#         evn.append(i)
#     else:
#         odd.append(i)
        
        
# print(odd) 
# print(evn)            

# print(A[::-1])

for i in A:
    print (i,end='')

A[2:4]= [555]
print(A)
    
str="hello how are you"
print(str.capitalize())
print(str.title())
print(str.split('r'))
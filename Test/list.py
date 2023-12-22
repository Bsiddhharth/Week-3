#ordered changable allow duplicate values


a=[1,2,3,4]

# print(a)
# print(a[1])
# print(a[1:])
# print(a[-1:])
# print(a[len(a)::-1])
# print(a[2::-1])


b=[5,6,7]
# print(a+b)

new=a+b

# print(new)
# new[0]=55

# print(new)
# new.append(78)  #appends to the end of the list 
# print(new)

# new.pop() #pops from the end of the list 
# print(new)

# new.pop(3)  #pops the element at 3rd index
# print(new)

c=[9,3,4,1,2,7]
c.sort()
print(c)

z=['a','v','w','b','c']

print(z)

# print(z[len(z)::-1])

#reverse of a list using append and pop
# rev=[]
# for i in range(len(z)):
#     rev.append(z.pop())

# print(rev)

# print(z)

#reversing a list  without any functions
for i in range(0,len(z)):
    for j in range(i+1,len(z)):
        z[i],z[j]=z[j],z[i]
    
print(z)    



    
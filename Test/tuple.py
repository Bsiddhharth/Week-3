#ordered unchangable allow duplicate values 
#dont forget ',' if only a single element is present

tup=(1,2,3)
print(type(tup))

tu=(9)         #not a tuple , to make it a tuple add a ','
print(type(tu))


a=tuple(('aa'))
print(a)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
print(thistuple[4::-1])
print(thistuple[-3::])  

#updating a tuple is only possible through 
#either coverting it to list
#adding another tuple to it

a=(1,2,3)
z=list(a)
z.append(8)
a=tuple(z)
print(a)

b=(1,2,3)
c=(4,5,6)
b+=c
print(b)

#same goes for removing an item from a tuple
#convert it to a list first

#deleting a tuple
cn=(1,2,3)
print(cn)
del cn
print(f"deleted {cn}")

#tuple unpacking
a=("color1","color2","color3",1,2,3,4,8,9,10)
(red,*orange,blue)=a

print(orange)  #two *'s are not possible 

#list of tuples
emp=[('abby',100),('bico',400),('karla',290)]

for name,hr in emp:
    print(name)
    print(hr)
   
   
   



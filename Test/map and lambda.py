def square(num):
    return num**2

my_num=[1,2,3,4]

# for i in map(square,my_num):
#     print(i)
    
print(list(map(square,my_num)))    
# for i in my_num:
#     print(square(i))



a=lambda num: num**2
print(a(4))


# using lambda fn in conjunction with square fn( using map)

numb=[1,2,3,4,5]
print(list(map(lambda num : num**2, numb)))

#using lambda fn in conjunction with square fn(using filter)

numb=[1,2,3,4,5]
print(list(filter(lambda num: num%2==0,numb)))


#to find square of a list of numbers using lambda and map

num=[1,2,3,4]
print(list(map(lambda num:num**2, num)))

#to return even ina  list of numbers using lambda and filter
numbers=[1,2,3,4,5,6]
print(list(filter(lambda num:num%2==0 , numbers)))
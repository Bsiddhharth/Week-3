a="hello"
b="hoi"
# b=4  #not possible to concatinate a string and number unless number is type-casted to string 
b=str(4)
print(a+" "+b)

#bool true for anything except empty and 0

print(bool("hi"))
v=''            #bool gives false
m=0              #bool gives you false
print(bool(v))


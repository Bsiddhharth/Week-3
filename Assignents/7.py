num=int(input("Enter an number : "))

# using for loop
for i in range(1,11):
    print(f"{i} * {num} = {num*i}")
    
#using while loop
j=1
while(j<11):
    print(f"{j} * {num} = {num*j}")
    j+=1    

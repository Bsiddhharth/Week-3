str=input("Enter a string to be checked whether palindrome or not : ")

flag=0
i=0
j=len(str)-1

while(i<j):
    if (str[i] != str[j]):
        flag=1    
    i+=1
    j-=1  

if(flag==0):
    print(f"{str} is a  palindrome")    
    
else:
    print(f"{str} is not a palindrome")    

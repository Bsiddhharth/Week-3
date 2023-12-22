#2d list or array

row=int(input("ENter the rows: "))
col=int(input("Enter the columns: "))

a=[]
print("Enter the array elements 1: ")
for i in range(row):
    l=[]
    for j in range(col):
        l.append(input())
        
    a.append(l)
        
        
b=[]
print("Enter the array elements 2: ")
for i in range(row):
    l=[]
    for j in range(col):
        l.append(input())
        
    b.append(l)
               
c=[]       
for i in len(a):
    for j  in len(b):
        c.append(a[j]+b[j])
    
print(c)         

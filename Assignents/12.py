row=int(input("Enter the no of rows : "))
col=int(input("Enter the no of columns : "))

a=[]
print("Enter the elements of array 1 : ")

for i in range(row):
    l=[]
    for j in range(col):
        l.append(int(input()))
    
    a.append(l)    
    
print("Enter the elements of array 2 : ") 
b=[]    
for i in range(row):
    l=[]
    for j in range(col):
        l.append(int(input()))
    
    b.append(l)    
    
c=[]    
for i in range(row):
    l=[]
    for j in range(col):
        l.append(a[i][j]+b[i][j])
    
    c.append(l)    
    
print(f"  {a} + ")
print(f"  {b} ") 
print(f"= {c}")   
    
        
        


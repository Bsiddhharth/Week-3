row=int(input("ENter te rows: "))
col=int(input("ENter te columns: "))

a=[]
print("Enter th elements in array: ")
for i in range(row):
    t=[]
    for j in range(col):
        t.append(int(input()))
    a.append(t) 
    
b=[]
print("Enter th elements in array: ")
for i in range(row):
    t=[]
    for j in range(col):
        t.append(int(input()))
    b.append(t)    
    
c=[]
print("Enter th elements in array: ")
for i in range(row):
    t=[]
    for j in range(col):
        t.append(a[i][j]+b[i][j])
    c.append(t)   
        
print(f"  {a} +")
print(f"  {b} ")
print(f"= {c}")   

        
def getarr(row,col):
    a=[]
    for i in range(row):
        t=[]
        for j in range(col):
            t.append(int(input(f"Enter the element at {i},{j} = ")))
            
        a.append(t)
        
    return a

def disparr(arr):
    print("Sum of array1 and array2 : ")
    for i in arr:
        print(i)        
          
def addarr(row,col,arr1,arr2):
    c=[]
    for i in range(row):
        t=[]
        for j in range(col):
            t.append(arr1[i][j] + arr2[i][j])    
        c.append(t)     
        
    return c    


row=int(input("Enter the size of row : "))
col=int(input("Enter the size of column : "))
arr1=[]
arr2=[]
sum=[]

arr1=getarr(row,col)    
arr2=getarr(row,col)
sum = addarr(row,col,arr1,arr2)
disparr(sum)
        
        

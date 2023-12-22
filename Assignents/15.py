def inputarr():
    n=int(input("Enter the size of array:"))
    
    a=[]
    for i in range(n):
        a.append(int(input(f"Enter element {i+1} : ")))
    
    return a

def disparr(arr):
    print("Array elements: ")
    for i in arr:
        print(i,end=' ')
        
        
arr=[]
arr=inputarr()
disparr(arr)        
        
        
        

# def fiba(n):
#     a,b=0,1
#     count=0

#     while count <n:
#         print(a,end=' ')
#         a,b=b,a+b 
#         count+=1
        
        
# n=10
# fiba(n)        
           
           
def fiba(n):
    a,b=0,1 
    c=0
    
    while c<n:
        print(a,end=" ")
        a,b=b,b+a
        c+=1
        
        
n=10
fiba(n)                   
           
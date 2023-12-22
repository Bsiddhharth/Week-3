def bub_sort(a):
    for i in range(len(a)):
        for  j in range(len(a)-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
# ----------------------------------------------- #
def ins_sort(a):
    for i in range(1,len(a)):
        j=i-1
        while j>=0 and a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            j-=1
    print(a)        
# ----------------------------------------------- #    
def sel_sort(a):
        for i in range(len(a)):
            min_val=i
            for j in range(i+1,len(a)):
                if a[j]>a[min_val]:
                    min_val=j
            a[i],a[min_val]=a[min_val],a[i]
        print(a)            
# ----------------------------------------------- #
a=[]
n=(int(input("enter the no of elements: ")))
for i in range(n):
    a.append(int(input(f"Enter element at  index {i} : ")))
    
bub_sort(a)    
ins_sort(a)
sel_sort(a)

    
    





    
            
                       
            
   
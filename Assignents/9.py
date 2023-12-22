n=int(input("Enter the size of array = "))
arr=[]

print("Enter the array elements : ")
for i in range(n):
    arr.append(int(input()))

print('')

num=int(input("ENter number to add to copy array : "))    

arr2=[]
for i in arr:
    arr2.append(i)
    
arr2.append(num)

print(f"Array1 = {arr}")
print(f"Array2 = {arr2}")    
    

    
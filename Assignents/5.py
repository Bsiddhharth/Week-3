print("Enter the total mark percentage = ",end="")
mark=float(input())

if mark>=90:
    print("grade : A")
    
elif mark>=80 and mark<90:
    print("grade : B")
    
elif mark>=70 and mark<80:
    print("grade : C")
    
elif mark>=60 and mark<70:
    print("grade : D")        
    
elif mark>=50 and mark<60:
    print("grade : E")        
   
else:
    print("Failed")    
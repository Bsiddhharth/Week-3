class menu:
    def add(self,a,b):
        print(f"{a} + {b} = {a+b}")
    
    def sub(self,a,b):
        print(f"{a} - {b} = {a-b}")
    
    def mul(self,a,b):
        print(f"{a} * {b} = {a*b}")
    
    def div(self,a,b):
        print(f"{a} / {b} = {a/b}")
                
obj=menu() 

while True:
    print("\nMENU")  
    print("1. Sum of two Numbers")  
    print("2. Difference between two Numbers")  
    print("3. Product of two Numbers")  
    print("4. Division of two Numbers")  
    print("5. Exit")  
    choice = int(input("\nEnter the Choice: ")) 
    
    if(choice==1):
        n1=float(input("Enter the number1 = "))
        n2=float(input("Enter the number2 = "))
        obj.add(n1,n2)
        
    elif(choice==2):
        n1=float(input("Enter the number1 = "))
        n2=float(input("Enter the number2 = "))
        obj.sub(n1,n2)    
        
    elif(choice==3):
        n1=float(input("Enter the number1 = "))
        n2=float(input("Enter the number2 = "))
        obj.mul(n1,n2)  
        
    elif(choice==4):
        n1=float(input("Enter the number1 = "))
        n2=float(input("Enter the number2 = "))
        obj.div(n1,n2)
        
    elif(choice==5):
        break          
    
    else:
        print("Enter a valid input") 
            
        
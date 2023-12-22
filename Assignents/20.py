from abc import ABC, abstractmethod

class Calculator(ABC): 
        @abstractmethod 
        def add (self,x,y): 
                pass
        @abstractmethod
        def sub(self, x, y):
                pass
        @abstractmethod
        def mul(self, x, y):
                pass
        @abstractmethod
        def div(self, x, y):
                pass
            
class BasicCalculator(Calculator):
    def add(self,a,b):
        print(a+b)            
        
    def sub(self,a,b):
        print(a-b)     
        
    def mul(self,a,b):
        print(a*b)        
        
    def div(self,a,b):
        if b==0:
            return "Division by zero not possible"
        print(a/b)         
        
calc = BasicCalculator()

while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter choice (1/2/3/4/5): ")

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            calc.add(num1, num2)
        elif choice == '2':
            calc.sub(num1, num2)
        elif choice == '3':
            calc.mul(num1, num2)
        elif choice == '4':
            calc.div(num1, num2)   
        elif choice == '5':
            print("Calculator exiting...")
            break
        else:
            print("Invalid input")


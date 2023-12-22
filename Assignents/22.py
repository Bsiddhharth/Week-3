class BankAccount:
    def __init__(self, name, account_number):
        self.__name = name  
        self.__account_number = account_number 

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
   
    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,new_num):
        self.__account_number=new_num
        
        
acc=BankAccount("AT",11)

print("Account Holder:", acc.name)
print("Account Number:", acc.account_number)        
        
acc.name="TT"        
acc.number=22

print("updt Account Holder:", acc.name)
print("updt Account Number:", acc.account_number)    
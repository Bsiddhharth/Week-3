
def switchcase(val):
    if val==1:
        print("Sunday")
    elif val==2:
        print("Monday") 
    elif val==3:    
        print("Tuesday")
    elif val==4:    
        print("Wednesday")
    elif val==5:    
        print("Thursday")    
    elif val==6:    
        print("Friday")
    elif val==7:    
        print("Saturday")    
    else:
        print("Invalid Entry")    


num=int(input("Enter a nunmber(1-7): "))
switchcase(num)
        
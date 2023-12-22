
v=900
def s():
    x=8
    # global v
    # v=888
    # print(v)
    def c():
        # nonlocal x
        x=90
        print(x)
        
    c()    
    print(x)    
    
s()  



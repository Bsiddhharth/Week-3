for i in range(10):
    if(i==6):
        break
    print(i)
    
    
for i in range(7):
    if(i==4):
        continue 
    print(i)   
    
    
#empty code is not allowed in any loop or functions so you can use pass their    
def fn():
    pass

for i in range(3):
    pass

while(i<10):
    pass

class mym:
    pass

print(type(mym))

p1=mym
print(type(p1))
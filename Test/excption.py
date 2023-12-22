def add(n1,n2):
  try:  
    print(n1+n2)
  except:
      print("Some error happened ...") 
  else:
      print("Runned succefully")     
    
    
n1=10
n2=input("Enter the number") 
# add(n1,int(n2))  
add(n1,n2)
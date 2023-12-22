x=5
y="hi"
z="Whatsup"

txt="1st-{} 2nd-{} 3rd-{} "              #format mathod
print(txt.format(x,y,z))            

print(f"1st-{x} 2nd-{y} 3rd-{z}")        #f string method

#format method but with order
bxt="{2}, {1}, {0}"
print (bxt.format(x,y,z))
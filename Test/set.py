#unordered unchangable unindexed , no duplicate elements
set1=set(("apple","blue","orange"))

print(set1)
set1.add("white")
print(set1)

set1.add("black")
print(set1)


#update method
#to add another set or list or any other 'DS' to a existing set

set2={"b","v","bb"}
# set2.update(set1)
# print(set2)

set3={90,78,67}
list1=[11,22,33]
set2.update(list1,set3) #cant initilize using update
set7=set2.union(set3,list1)
print(set2)
print(set7)#both update and union excludes duplicate 


#remove() vs discard() 
#remove produces an error if no item to remove but for discard
#no error will rise if such an element to delete is absent

set4={1,2,3,4}
# set4.remove(5)
# print(set4)

set4.discard(5)
print(set4)

#clear() will clear out the set
#whereas del() will delete the set completely

# -------------------------- #

#to keep only duplicates

x = {"apple", "banana", "cherry",11}
y = {"google", "microsoft",11, "apple"}

x.intersection_update(y)

print(x)

v=x.intersection(y)#to assign
print(v)
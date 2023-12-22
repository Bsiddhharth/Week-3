import functools
letters=["h","e","l","l","O"]

word=functools.reduce(lambda x,y: x+y ,letters)

print(word)

# factorial=[1,2,3,4,5]
# # factorial.append(lambda x: x for x in range(1,6))
# fact=functools.reduce(lambda x,y : x*y,factorial)


# print(factorial)

# one parameter square of x
print((lambda x:x**2)(3))

#multiple parameter add of x and y
print((lambda x,y:x+y)(2,3))

#first element in list
print((lambda l:l[0])([3,4,5]))

#concat string
print((lambda s1,s2:s1+s2)("a","v"))

# assigning name to function

fun=(lambda x:x+10)
print(fun(3))
#Recursive Functions :
# It must have breaking condition or else it will become an infinite loop



# Write function take list as parameter, from function change first value of list to 10
# after function call print the list


def li(lise:list):
    lise[0]=10
    print(lise)
l=[1,2]
li(l)

print(l)
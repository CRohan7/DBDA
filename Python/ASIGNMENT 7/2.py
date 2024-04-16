#Q WA function to take list as parameter
#  and print all numbers of given list which are divisible by 11


def check(l:list):
    for i in l :
        if((i%11)==0):
            print(i , end=' ')
        
l=[1,2,33,4,5,11]
check(l)



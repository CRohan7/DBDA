# 15. Write a Python program that accepts a 
# hyphen-separated sequence of words as 
# input and prints the words in a 
# hyphen-separated sequence after sorting
# them alphabetically. 
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow


def check(s:str):
    s=s.split('-')
    s=sorted(s)
    print( "-".join(s) )


s="green-red-yellow-black-white"
check(s)

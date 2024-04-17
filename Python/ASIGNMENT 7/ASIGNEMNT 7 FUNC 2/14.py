# 14. Write a Python function to check whether a string is a pangram or not. 
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"


def check(s:str):
    s=s.lower() # convert str to lower case
    s=s.split() # split to eliminate spaces 
    s="".join(s) # join together as one string 
    print(s) 
    l1=[]
    for i in s:
        l1.append(ord(i)) # convert string into list of character's ascii code
    print(l1)     
    l1=set(l1) #convert into set to eliminate duplicate characters
    l1=list(l1) #convert unique values to list
    print(len(l1))

    if(len(l1)==26):   # if all characters len = 26 then all characters are present 
        print("Its Palgram!")
    else:
        print("Try Better!!")


s=input("Enter String: ")
check(s)
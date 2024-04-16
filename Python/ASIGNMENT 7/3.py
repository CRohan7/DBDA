# Q WA function to take string as parameter
# Check if string is palindrome or not
# If palindrome return 1
# if not palindrome return 0

def check(name:str):
    new=name[::-1]
    #new.lower()
    if(name==new):
        return 1
    else:
        return 0




name=input("Enter Name: ")

s=check(name)
print(s)

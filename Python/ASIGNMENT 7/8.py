# Q WA function to take list of strings 
# as parameter and print all strings which have character 's' 2 times

def check(s:str):
    
    for i in l:
        count=0
        for s in i:
            if s=='s':
                count+=1
        if count==2:
            print(i)


l=['ss','fss','lss','shs','ls']

check(l)

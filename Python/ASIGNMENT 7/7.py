# Q WA function to take a dictionary as parameter. 
# Print value of key "name" if key "rollno" is having value 100.


def check(d:dict):
    
    if d["rollno"] == 100:
        print(d["name"])


d={'marks':7,'name':'gjhgjhgh', 'rollno':100}
check(d)

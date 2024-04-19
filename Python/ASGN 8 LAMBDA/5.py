"""
Q. Take Employee id and Employee name of 5 employees from user. Store it in dictionary. 
Print all employees in increasing order of employee Id . Also print all employees in alphabetical
 order by name.
    
    for i in range(5):
    name=input("Enter Name: ")
    idd=input("Enter Id: ")
    dic[idd]=name
"""
dic ={'7': 'Rohan', '8': 'Sohan', '23': 'Kohan', '4': 'Mohan', '98': 'Yohan'}
# for id
print(sorted(dic.items(), key=(lambda x:(x[0]))))

# for name
print(sorted(dic.items(), key=(lambda x:(x[1]))))




 
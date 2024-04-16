#Q WA function to take list of dictionaries. 
# Print all dictionaries which contain key "id".


def check(ll:list):
    for i in ll:
        for j in i:
            if j=='idd':
                print(i)


l=[ {1:'s'},{2:'r'},{3:'f'},{'idd':7} ]
check(l)



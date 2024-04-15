"""
1. Given a string of odd length greater than 7, return a new string made of the middle three characters
of a given String
Given:
str1 = "RakeshzipPetabb"
Output
zip
str2 = "JazzbonAyxx"
Output
bon


"""

"""
str1 = "RakeshzipPetabb"
str2 = "JazzbonAyxx"


#str1
l=len(str1)
mid=int((l+1)/2)-1
lmid=mid-1
rmid=mid+1
new=str1[lmid]+str1[mid]+str1[rmid]
print(new)


# str2
l=len(str2)
mid=int((l+1)/2)-1
lmid=mid-1
rmid=mid+1
new=str2[lmid]+str2[mid]+str2[rmid]
print(new)


"""
str1 = "RakeshzipPetabb"
mid=str1[len(str1)//2]
lmid=str1[(len(str1)//2) -1]
rmid=str1[(len(str1)//2) +1]


print(lmid+mid+rmid)



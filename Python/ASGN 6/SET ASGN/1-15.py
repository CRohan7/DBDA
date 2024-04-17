"""
#1

s={1,2,3}

#2
for i in s:
    print(i)

#3
s.add(4)
s.add(5)
print(s)

#4
s.remove(5)
print(s)



#6
s1={1,2,3,4}
s2={4,6,7,8}
s3=s1.intersection(s2)
print(s3)


#7
s1={1,2,3,4}
s2={4,2,6,7,8}

s3=s1.union(s2)
print(s3)

#8
s1={1,2,3,4}
s2={4,2,6,7,8}

s3=s1.difference(s2)
print(s3)

s4=s2.difference(s1)
print(s4)

#9
s1={1,2,3,4}
s2={4,2,6,7,8}

s3=s1.symmetric_difference(s2)
print(s3)   #excluding 2,4

#10

s1={2,4}
s2={4,2,6,7,8}

if(s1.issubset(s2)):
    print("S1 subset of S2!")

#11

s1={2,9,4,2,6,7,8}
#shallow copy
s2=s1.copy()
print(s2)

#12
s1={2,9,4,2,6,7,8}

s1.clear()

print(s1)


#13

fs=frozenset([1,2,3,4,5])
print(fs)

#14

s1={2,9,4,2,6,7,8}
print("Min:" , min(s1) , "\nMax:",max(s1))
"""

#15

s1={2,9,4,2,6,7,8}

print( "LENGTH:",len(s1))







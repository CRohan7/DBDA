"""
#1
# sorting on basis of keys
d={30:100,1:20,2:30 }
print(sorted(d))

#2
#add element
d={0: 10, 1: 20}
d[2]=30
print(d)

#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1|dic2|dic3

#4
dic1={1:10, 2:20}
key=int(input("Enter Key: "))
if key in dic1:
    print("Exists")
else:
    print("Not Exists")
    

#5
dic1={1:10, 2:20}
for i in dic1:
    print(i)
"""

#6 

num=int(input("Enter Number: "))
s=[]
s2=[]

for i in range(1,num+1):
    s.append(i)
print(s)

for i in range(1,num+1):
    s2.append(i*i)
print(s2)

s3=dict(zip(s,s2))
print(s3)





"""
#15
d={1:10,2:-60,5:-30,7:20}
v=d.values()
print( min(v))
print( max(v))


#or

d={1:10,2:60,5:30,7:20}
l=[]
for i in d.values():
    l.append(i)
l.sort(reverse=True)
print("Max:",  l[0])
print("Min ", l[len(d)-1])

#16
#Yet to be Taught

#17
#There cannot be duplicate keys in dictionary

#18
d={1}
if(bool(d)):
    print("Not Empty")
else:
    print("Empty")

"""
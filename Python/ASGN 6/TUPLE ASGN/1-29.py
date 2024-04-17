'''
#1

t=(1,2,3,4,5)
print(t)

#2
t=(1,1.11,'c','CR',True)
print(t)

#3
t=(1,2,3,4,5,6,7,8,9)
print(t[0])

#4
x,y,*z=t
print(x,'|',y,'|',*z)

#5
#cannot add in tuple

#6
t=('R','O','H','A','N')
s=''
for i in t:
    s=s+i
print(s)
#8
t=((1,2,3),3,4)
print(t)

#7 
t=(1,2,3,4,5,6,7,8,9)
print(t[-4])

#9
t=(1,2,4,3,5,4,5,1)
count=0
for i in t:
    count=0
    for j in t:
        if(i==j):
            count+=1
    if(count>1):
        print(i)

        OR
t1=(9,9,9,9,23,45,67,67,10)
repeateed_set=set()
for inx1 in range(len(t1)):
    for inx2 in range(len(t1)):
        if (inx1!=inx2) and (t1[inx1]==t1[inx2]) and (t1[inx1] not in repeateed_set):
                             repeateed_set.add(t1[inx1])
print(repeateed_set)
 
#10
while(1):
    num=int(input("Enter No To Search: "))
    t=(1,2,3,4,5,6)
    if(t.count(num)>0):
        print("It exists!")
    else:
        print("Not Exists!")

  

#11

l=[1,2,3,4,5]
t=tuple(l)
print(t)    
 

#12 cant modify into tuple

#13
t=('P','U','N','E')
print(t[:2])

#14

t=('P','U','N','E')
print(t.index('N'))

#15
t=('P','U','N','E')
print(len(t))


#16
t=('0P','1U','2N','3E')
d=dict(t)
print(d)


#17
t=(12,23,34,45,56)
for i in t:
    print(i)


#18
t=(1,2,3,4,5,6,7,8,9,10)
t1=t[::-1]
print(t1)


#19

t=([1,2],[3,4],[5,6])
d=dict(t)
print(t) 

#23
t=(('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'))
l=[t[1] for i in t]
print(l)


#20
t=(100, 200, 300)

s='This is a tuple'

print(s,t)

#21

l=[(10,20,40),(40,50,60),(70,80,90)]
print(l)
new_l=[]
f_list=[]
for i in range(len(l)):
    new_l=list(l[i])
    
    new_l[-1]=100

    new_t=tuple(new_l)
    f_list.append(new_t)
print(f_list)  


#22
l=[(), () ,('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
l1=l.copy()
print(len(l))
print(l)
for i in range(len(l1)):
    print(bool(l1[i]))
    if(bool(l1[i])==False):
       l.remove(l1[i])

print(l)




#25
s='python3.0'
t=tuple(s)
print(t)




#26
t=(4, 3, 2, 2, -1, 18)
l=[]

num=10
for i in range(len(t)):
    l.append(t[i]*num)

t=tuple(l)
print(t)




#27
t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
sum=0
avg=0
l=[]
for i in t:
    le=len(i)
    for j in i:
        sum=sum+j
        avg=sum/le
    l.append(avg)
    
print(l)


#28
t=(('333', '33'), ('1416', '55'))

l=[]
lmin=[]
for i in t:
    for j in i:
         
        c=int(j)
        lmin.append(c)

    print()
    print(lmin)
        #l.append(c)
        #t=tuple(l)


#29
t=(1,2,3)
s=''
for i in t:
    i=str(i)
    s=s+i 
s=int(s)
print(s)


while(1):
    t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
    ele=input("Enter Element To Be Searched: ")
    for i in t:
        for j in i :
            if(ele==j):
                print("True")
                break
            else:
                print("False")
                break
'''



















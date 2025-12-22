
l1=[1,2,3,6,4,8,5,2,3,9,1,10,15,40,99,43,66,8,99,10,3,2]
print(l1)
l2=[]
l3=[]
l4=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

for i in l2:
    l2.sort()
print(l2)


print(l2[0],"is the min number of the list")
print(l2[1],"second min number of the list")
print(l2[-2],"max number of the list")
print(l2[-1],"second max number of the list")

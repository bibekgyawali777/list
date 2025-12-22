
l1=[1,3,5,-2,-4,8,-9,-15,20]

for i in l1:
    if i<0:
      x=l1.index(i) 
      l1.pop(x) 
      l1.insert(x,0)
print(l1)
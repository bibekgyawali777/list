n=int(input("enter how many num do you want : "))
l1=[]

for i in range(n):
    value= int(input("enter number : "))
    l1.append(value)
print("list","=",l1)

sum=0
for i in l1:
        l1.sort()
        sum+=i
        average=sum/n
print("sum is","=",sum)
print("max number is","=",l1[-1])   
print("min number is","=",l1[0]) 
print("average is","=",average)
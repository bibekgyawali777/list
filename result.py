
n= int(input("enter how many subject do you have : "))
l1=[]
for i in range(n):
    a=float(input(f"enter subject{i+1} mark : "))
    l1.append(a)
print("mark","=",l1)
total=0
for i in l1:
    total+= i
    average=total/n

    percentage= (total/(n*100))*100
print("total mark","=",total)
print("average","=",average)

if percentage >=50:
    if 50<= percentage <60 :
        print("your percentage is","=",percentage)
        print("your grade is : c")
    elif 60<= percentage <70 :
        print("your percentage is","=",percentage)
        print("your grade is : B")
    elif 70<= percentage <80 :
        print("your percentage is","=",percentage)
        print("your grade is : A")
    elif 80<= percentage <=100 :
        print("your percentage is","=",percentage)
        print("your grade is : A+")
    print("you are pass")
else:
    print("you are fail")
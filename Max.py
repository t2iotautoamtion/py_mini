n=int(input("Enter the list size:"))
a=[]
for i in range(n):
    num=int(input("enter the number:"))
    a.append(num)
print(a)
max=a[0]
for i in range(n):
    if(max<a[i]):
        max=a[i]
print("Maximum",max)
    

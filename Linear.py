n=int(input("Enter the no.of elements:"))
i=0
a=[i for i in range(n)]
for i in range(0,n):
    a[i]=int(input("Enter the Elements:"))
for i in range(0,n):
    print(a[i])
key=int(input("Enter the Elements to be searched:"))
for i in range(0,n):
    if a[i]==key:
        print("Key found")

                                                                                  

def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter a first number:"))
b=int(input("Enter a Second number:"))
print(gcd(a,b))

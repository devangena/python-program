a=int(input("type the first number:"))
b=int(input("type the second number:"))
while b!=0:
    r=a%b
    a=b
    b=r
print("the GCD of the number is",a)
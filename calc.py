n=int(input("enter the choices from 1 to 4:"))
a=int(input("enter the first num:"))
b=int(input("enter the second num:"))
if n==1:
    c=a+b
    print("sum is",c)
elif n==2:
    c=a-b
    print("difference is",c)
elif n==3:
    c=a*b
    print("Product is",c)
elif n==4:
    c=a/b
    print("Quotient is",c)
else:
    print("Invalid Choice")            
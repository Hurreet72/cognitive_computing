a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("a is greater")
elif b>c and b>a:
    print("b is greter")
elif c>b and c>a:
    print("c is greater")
else:
    print("they are equal")           
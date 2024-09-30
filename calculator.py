a=float(input("Enter first digit: "))
op=input("Enter operator (+, -, *, /): ")
b= float(input("Enter second digit: "))

if op == "+":
    c=a+b
    print(c)
elif op == "-":
    d=a-b
    print(d)
elif op == "*":
    e=a*b
    print(e)
elif op == "/":
    if b == 0:
        print ("oh no")
    f=a/b
    print(f)

else:
    print("invalid")

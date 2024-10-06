while True:
    a=input("Enter first digit or e to exit: ")
    if a=='e':
        break
    op=input("Enter operator (+, -, *, /) or e to exit: ")
    if op=="e":
        break
    b=input("Enter second digit or e to exit: ")
    if b=="e":
        break

    h=float(a)
    i=float(b)

    if op == "+":
        c=h+i
        print(c)
    elif op == "-":
        d=h-i
        print(d)
    elif op == "*":
        e=h*i
        print(e)
    elif op == "/":
        if i == 0:
            print ("oh no")
        f=h/i
        print(f)
    g= float(input("would you like to continue? click 1 for yes and 0 for no"))
    if g==1:
        continue
    if g==0:
        break
    else:
        print("invalid")
print("thank you for your business")

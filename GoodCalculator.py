while True:
    h= str(input("enter a to exit and any letter to countinue"))
    a=float(input("Enter first digit: "))
    h= str(input("enter a to exit and any letter to countinue"))
    op=input("Enter operator (+, -, *, /): ")
    h= str(input("enter a to exit and any letter to countinue"))
    b= float(input("Enter second digit: "))
    h= str(input("enter a to exit and any letter to countinue"))

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
    g= float(input("would you like to continue? click 1 for yes and 0 for no"))
    if g==1:
        continue
    if g==0:
        break
    else:
        print("invalid")
    if h=="a":
        break
    
a= int(input("What should I convert to? Celcius or fahrenheit? If input 0 then celcius and 1 then fahrenheit."))
if a==0:
    b= float(input("What tempreture do u want in fahrenheit?"))
    c= (b*9/5)+32
    print(c)
else:
    e= float(input("What temperature do u want in celcius?"))
    d= 5/9*(e-32)
    print(d)



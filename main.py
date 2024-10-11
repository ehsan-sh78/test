a = int(input("enter your first number: "))
b = int(input("enter your second number: "))
c = str(input("enter your function (+ - / *): "))

if c!="+" and c!="-" and c!="/" and c!="*":
    print("invalid function")
else:
    if c=="/" and b==0:
        print("unknown")
    else:
        if c=="+":
            print(a+b)
        elif c=="-":
            print(a-b)
        elif c=="/":
            print(a/b)
        elif c=="*":
            print(a*b)


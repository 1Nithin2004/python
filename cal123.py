#basic calculator
def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter operation[+,-,*,/]:"))
if c=="+":
    print(a,"+",b,"=",add(a,b))
elif w=="-":
    print(a,"-",b,"=",sub(a,b))
elif w=="*":
    print(a,"*",b,"=",multiply(a,b))
elif w=="/":
    print(a,"/",b,"=",divide(a,b))

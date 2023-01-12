def palindrome(a):
     p=''
     for i in a:
            if i.isalnum():
                if i.isalpha:
                    p+=i.lower()
                else:
                    p+=i
     return (p==p[::-1])
a=(input("enter the number:"))
s=palindrome(a)

if s:
    print("true")
    
else:
    print("false")
    

#Say "Hello, World!" With Python
print("Hello, World!")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)
    
#Python If-Else
if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2!=0: #odd
        print("Weird")
    else:
        if n>20:
            print("Not Weird")
        elif n>=6:
            print("Weird")
        else:
            print("Not Weird")
            
#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a//b)
    print(a/b)
        

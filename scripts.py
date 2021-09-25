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
        
#Loops
if __name__ == '__main__':
    n = int(raw_input())
    x=0
    while x<n:
        print(x*x) 
        x=x+1
        
#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        leap=True
        if year%100==0:
            leap=False
            if year%400==0:    
                leap=True
    return leap

year = int(raw_input())

#Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    s=""
    for i in range(1,n+1):
        s=s+str(i)
    print(s)

 #List Comprehensions
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
    l=[[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
    print(l)
    
  #Nested Lists
if __name__ == '__main__':
    #creo lista di liste
    #ottengo il valore minimo m, e  k il numero di volte che compare 
    l=[]
    mini=float("inf")
    num=1
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        l.append([name,score])
        if mini>score:
            mini=score
            num=1
        elif mini==score:
            num+=1
    #ordino la lista in modo crescente
    #elimino i primi k valori
    #prendo il valore minimo m2, e estraggo dalla lista e print fino a quando l[next]=m2 
    l=sorted(l,key=lambda x: x[1])
    l=l[num:]
    min2=l[0][1]
    x=0
    name=[]
    while (x<len(l) and l[x][1]==min2 ):
        name.append(l[x][0])
        x+=1
    name.sort()
    for el in name:  
        print(el)  

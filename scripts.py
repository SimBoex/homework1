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
        
#Finding the percentage
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    
    punteggio=student_marks[query_name]
    sum=0
    lenght=len(punteggio)
    for el in punteggio:
        sum+=el
    sum=sum/lenght
    print(format(sum, '.2f'))  
    
#Find the Runner-Up Score!    
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    mas=arr[-1]
    while n-1>=0 and arr[n-1]==mas:
        arr.pop()
        n-=1 
    print(arr[n-1])
    
#Lists
if __name__ == '__main__':
    list=[]
    x=0
    N = int(raw_input())
    while x<N:
        comando= str(raw_input())
        lista=comando.split()
        com=lista[0]
        valori=lista[1:]
        if com=="insert":
             list.insert(int(valori[0]),int(valori[1]))
        elif com=="print":
             print(list)
        elif(com=="remove"):
             list.remove(int(valori[0]))
        elif(com=="append"):
             list.append(int(valori[0]))
        elif(com=="sort"):
             list.sort()
        elif(com=="pop"):
             list.pop()
        elif(com=="reverse"):
             list.reverse()
        x+=1
        
#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))

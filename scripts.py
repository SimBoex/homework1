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

#sWAP cASE
def swap_case(s):
    s=s.swapcase()
    return s

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
    
#String Split and Join
def split_and_join(line):
    # write your code here
    return "-".join(line.split())

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
    
#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
    
#Mutations
def mutate_string(string, position, character):
    string=string[0:position]+character+string[position+1:]
    return string

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new
    
#Find a string
def count_substring(string, sub_string):
    inizio=sub_string[0]
    add=True
    intero=0
    for char in range(0,len(string)):
        if string[char]==inizio and char+len(sub_string)-1<len(string):
            ck=1
            while ck<len(sub_string) and add:
                if string[char+ck]!=sub_string[ck]:
                    add=False
                ck+=1
            if add:
                intero+=1
            add=True
     
    return intero

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

#String Validators
if __name__ == '__main__':
    s = raw_input()

isalnum=False
isalpha=False
isdigit=False
lower=False
upper=False
for char in s:
    if  not isalnum and char.isalnum() :
        isalnum=True
    if not isalpha and char.isalpha():
        isalpha=True
    if not isdigit and char.isdigit():
        isdigit=True
    if not lower and char.islower():
        lower=True
    if not upper and char.isupper():
        upper=True
        
print(isalnum)
print(isalpha)
print(isdigit)
print(lower)
print(upper)

#Text Wrap
import textwrap

def wrap(string, max_width):
    result=""
    numero=len(string)/max_width
    for i in range(0,round(numero)+1):
        result=result+string[i*max_width:(i+1)*max_width]+"\n"
    result=result[:-1]
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#String Formatting
def print_formatted(number):
    # your code goes here
    lunghezza = len("{0:b}".format(number))
    for i in range(1,number+1):
        print ("{:{lar}d} {:{lar}o} {:{lar}X} {:{lar}b}".format(i,i,i,i, lar=lunghezza))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#Capitalize!    
def solve(s):
    l=s.split(" ")
    for pos in range(len(l)):
        l[pos]=l[pos].capitalize()
    stringa=" ".join(l)
    return stringa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
#Introduction to Sets
def average(array):
    # your code goes here
    insieme=set(array)
    mas=sum(insieme)
    return mas/len(insieme)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
#Symmetric Difference
if __name__ == '__main__':
    n1=int(input())
    l1=input().split()
    s1=set(l1)
    n2=int(input())
    l2=input().split()
    s2=set(l2)
    diff1=s1.difference(s2)
    diff2=s2.difference(s1)
    res=diff1.union(diff2)
    l=[]
    for el in list(res):
        l.append(int(el))
    l=sorted(l)
    for el in l:
        print(el)
        
#Set .add()
n=int(input())
s=set()
for row in range(n):
    nome=str(input())
    s.add(nome)
print(len(s))
   
#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
num=int(input())
for el in range(num):
    row=input().split()
    if len(row)>1:
        valore=int(row[1])
        if row[0]=="discard":
            s.discard(valore)
        else:
            s.remove(valore)
    else:
        s.pop()
somma=sum(s)
print(somma)

#Set .union() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
tot=s1.union(s2)
print(len(tot))

#Set .intersection() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
inter=s1.intersection(s2)
print(len(inter))

#Set .difference() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
print(len(s1-s2))

#Set .symmetric_difference() Operation
n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
print(len(s1.symmetric_difference(s2)))

#Set Mutations
n1=int(input())
s1=set(map(int,input().split()))
righe=int(input())
for el in range(righe):
    comando=str(input().split()[0])
    s2=set(map(int,input().split()))
    if comando=="intersection_update":
        s1.intersection_update(s2)
    elif comando=="update":
        s1.update(s2)
    elif comando=="symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    else:
        s1.difference_update(s2)
print(sum(s1))

#The Captain's Room
n1=int(input())
s1=list(map(int,input().split()))
in1=set()
in2=set()
for el in s1:
    if el not in in1:
        in1.add(el)
    elif el  in in1:
        in2.add(el)
res=in1-in2
print(res.pop())

#Check Subset
t=int(input())
for el in range(t):
    n1=int(input())
    s1=set(map(int,input().split()))
    n2=int(input())
    s2=set(map(int,input().split()))
    if len(s1-s2)==0:
        print(True)
    else:
        print(False)

#Check Strict Superset
s1=set(map(int,input().split()))
n1=int(input())
val=True
for el in range(n1):
    s2=set(map(int,input().split()))
    if len(s1-s2)>=1 and len(s2-s1)==0:
        val=True
    else:
        val=False
        break
print(val)

#No Idea!
n,m=input().split()
n=int(n)
m=int(m)
l=list(map(int,input().split()))
s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
cont=0
for el in l:
    if el in s1:
        cont+=1
    elif el in s2:
        cont-=1
print(cont)

#collections.Counter()
from collections import Counter
n1=int(input())
c=Counter(map(int,input().split()))
n=int(input())
tot=0
for el in range(n):
    row=input().split()
    taglia,costo=row
    if c[int(taglia)]>0:
       tot+=int(costo)
       c[int(taglia)]=c[int(taglia)]-1 
print(tot)

#Collections.OrderedDict()
from collections import OrderedDict
n=int(input())
diz=OrderedDict()
for el in range(n):
    *item,costo=input().split()
    item=" ".join(item)
    if item not in diz:
        diz[item]=int(costo)
    else:
        diz[item]+=int(costo)
        
for item,costo in diz.items():
    print("{} {}".format(item,costo))

#Collections.namedtuple()
from collections import namedtuple
n=int(input())
head=input().split()
l=[]
for el in range(n):
    Point2= namedtuple("head",head)
    riga=input().split()
    s=Point2(riga[0],riga[1],riga[2],riga[3])
    l.append(s)
sum=0
for el in l:
    t=int(getattr(el,'MARKS'))
    sum+=t

print(sum/n)
    
#Collections.deque()
from collections import deque
d=deque()
n=int(input())
for el in range(n):
    commando=input().split()
    if len(commando)>1:
        if commando[0]=="appendleft":
            d.appendleft(commando[1])
        elif commando[0]=="append":
            d.append(commando[1])
    else:
        if commando[0]=="popleft":
            d.popleft()
        else:
            d.pop()            
print(" ".join(d))

#DefaultDict Tutorial
from collections import defaultdict
d = defaultdict(list)
n,m=map(int,input().split())
for el in range(n+m):
    stringa=input()
  
    if el<n:
        if stringa not in d:
            d[stringa].append(el+1)
        else:
            d[stringa].append(el+1)
    
    else:
        if stringa in d:
            for c in d[stringa]:
                print(c,end=" ")
            print()
        else:
            print(-1)
            
#Calendar Module
import calendar
mese,giorno,anno=map(int,input().split())
giorni= ['MONDAY', "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(giorni[calendar.weekday(anno, mese, giorno)])

#Exceptions
n=int(input())
for el in range(n):
    try:
        a,b=map(int,input().split())
        div=a//b
        print(div)
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e1:
        print("Error Code:",e1)

#Zipped!
n,x=map(int,input().split())
l=[]
for  el in range(x):
    row=map(float,input().split())
    l.append(row)

f=zip(*l)
for el in f:
    tot=sum(el)/len(el)
    print(tot)
    
#Athlete Sort   
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr.sort(key=lambda x:x[k])
    for el in arr:
        print(*el,sep=" ")

#ginortS

stringa=input()
even=[]
odd=[]
lower=[]
upper=[]

for char in stringa:
    if char.isdigit() and int(char)%2==0:
        even.append(char)
    elif char.isdigit():
        odd.append(char)
    elif char.islower():
        lower.append(char)
    else:
        upper.append(char)
            
even.sort()
odd.sort()
lower.sort()
upper.sort()
finale=""

for el in [lower,upper,odd,even]:
    if el:
       finale=finale+"".join(el) 
print(finale)

#Map and Lambda Function
cube = lambda x:x*x*x # complete the lambda function x

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n>1:
        l=[0,1]
        for el in range(2,n):
            valore=l[el-1]+l[el-2]
            l.append(valore)
    return l

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

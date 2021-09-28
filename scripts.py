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

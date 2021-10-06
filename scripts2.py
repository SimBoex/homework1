
#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    cont=0
    max=0
    for el in candles:
        if max<el:
            max=el
            cont=1
        elif max==el:
            cont+=1
    return cont
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    
    
#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1<v2:
        slower=v1
        faster=v2
    else:
        slower=v2
        faster=v1
    if x1<x2:
        far=x1
        ahead=x2
    else:
        far=x2
        ahead=x1
    if (far==x1 and slower==v1):
        return "NO"
    if (far==x2 and slower==v2):
        return "NO"
    while far<ahead:
        far+=faster
        ahead+=slower
        if far==ahead:
            return "YES"
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
    
#Viral Advertising
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    #creo array di tuple
    #ogni giorno faccio utilizzo il giorno precedente per calcolare
    a=[2]
    inizio=2
    for el in range(1,n):
        valore=math.floor(inizio*3/2)
        a.append(valore)
        inizio=valore
    return sum(a)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    n=str(n)
    tot=0
    for char in n:
        tot+=int(char)
    tot=tot*k
    tot=str(tot)
    cont=0
    while len(tot)!=1:
        for char in tot:
            cont+=int(char)
        tot=str(cont)
        cont=0
    return int(tot)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

    
#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value=arr[n-1]
    index=n-2
    while index>=0:
        if arr[index]<value: 
            arr[index+1]=value
            print(*arr)
            break

        elif arr[index]>=value: 
            arr[index+1]=arr[index] 
            print(*arr)
        if index==0:
            arr[0]=value
            print(*arr)    
        index=index-1
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

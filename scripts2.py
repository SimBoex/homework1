
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

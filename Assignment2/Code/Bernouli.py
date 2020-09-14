import numpy as np
import random

sample_size=200

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
num=Rand(10000000,99999999,sample_size)
print("random numbers are",num)

index=random.randint(0,199)
number=num[index]
print("\n A random integer among the numbers generated is", number)

digit=np.array([0,1,2,3,4,5,6,7,8,9])
Frequency=np.array([22,26,22,22,20,10,14,28,16,20])

def lastDigit(n) : 
    # return the last digit 
    return (n % 10)

n=lastDigit(number)
print("\n Last digit of",number,"is",n)

def checkIndexDigit(n):             #check position of last digit in digit matrix
    c=0
    for i in range(0,len(digit)):
        if digit[i]==n:
            c=i
    return c;

def checkValueFreq(k):          #accordingly check value of frequency of last digit
    freq=Frequency[k]
    return freq;

indexInDigitArray=checkIndexDigit(n)
freqOfDigit=checkValueFreq(indexInDigitArray)

probability=freqOfDigit/sample_size
print("Probability of unit digit",n,"in entered number",number,"is:",probability)

"""
Created on Sat Sep 12 22:32:41 2020
Generate 200 numbers and find probability of any random digit
@author: Rubeena
"""
import numpy as np
import random

sample_size=200

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
number=Rand(1,99999999,sample_size)
print("random numbers generated are",number)

digit=np.array([0,1,2,3,4,5,6,7,8,9])
Frequency=np.array([22,26,22,22,20,10,14,28,16,20])

def FindFreqTable(unitDigits,digit):          #accordingly check value of frequency of last digit
    freq=np.zeros((len(digit),),dtype='int')
    for i in range(0,len(unitDigits)):
        for j in range(0,len(digit)):
            if unitDigits[i]==digit[j]:
                c=j
                freq[c]+=1
    return freq;

def LastDigitArray(number):
    lastDigit = []
    for i in range(0,len(number)):
        lastDigit.append(number[i]%10)
    return lastDigit;

unitDigits=LastDigitArray(number)
print("Last digits of each of these numbers generated are:\n",unitDigits)

freq=FindFreqTable(unitDigits,digit)
print("frequency distribution table \n", freq)


def checkValueFreq(index):          #accordingly check value of frequency of last digit
    frequen=freq[index]
    return frequen;

#Chose a random last digit
index=random.randint(0,len(digit))
print("\n A random last digit chosen \n", index)

freqOfDigit=checkValueFreq(index)

probability=freqOfDigit/sample_size
print("Probability of unit digit",index,"is:",probability)

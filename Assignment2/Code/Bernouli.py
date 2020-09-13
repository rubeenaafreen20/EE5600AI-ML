import numpy as np

sample_size=200

digit=np.array([0,1,2,3,4,5,6,7,8,9])
Frequency=np.array([22,26,22,22,20,10,14,28,16,20])
number=int(input("Enter any single digit number to find its probability  \n"))

def lastDigit(number) :
    single=0
    # return the last digit 
    if (number/10)<1:
        single=1
    else:
        single=2
    return single;
    
def checkIndexDigit(number):             #check position of last digit in digit matrix
    c=0
    for i in range(0,len(digit)):
        if digit[i]==number:
            c=i
    return c;

def checkValueFreq(k):          #accordingly check value of frequency of last digit
    freq=Frequency[k]
    return freq;

n=lastDigit(number)
if n==1:
    indexInDigitArray=checkIndexDigit(number)
    freqOfDigit=checkValueFreq(indexInDigitArray)
    probability=freqOfDigit/sample_size
    print("Probability of digit",number,"at unit place is:",probability)

else:
    print("Please enter a single digit number")
    

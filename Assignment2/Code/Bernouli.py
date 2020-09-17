"""
Created on Sat Sep 12 22:32:41 2020
Generate 200 random numbers and find probability of each digit
@author: Rubeena
"""
import numpy as np
import pandas as pd

sample_size=200
 
number=np.random.randint(1, 99999999, size=sample_size)
print("random numbers generated are",number)

#Frequency distribution table as given in the problem in Excel sheet
digit=np.array([0,1,2,3,4,5,6,7,8,9])
Frequency=np.array([22,26,22,22,20,10,14,28,16,20])

def FindFreqTable(unitDigits,digit):          #accordingly check value of frequency of last digit
    freq1=np.zeros((len(digit),),dtype='int')
    for i in range(0,len(unitDigits)):
        for j in range(0,len(digit)):
            if unitDigits[i]==digit[j]:
                c=j
                freq1[c]+=1
    return freq1;

def LastDigitArray(number):
    lastDigit = []
    for i in range(0,len(number)):
        lastDigit.append(number[i]%10)
    return lastDigit;

#Enter Random numbers and their last digits into excel sheet
unitDigits=LastDigitArray(number)

#This part prints frequency of each digit on console.
#Used only for comparison purpose
#frequen=FindFreqTable(unitDigits,digit)
#d2=pd.Series(frequen)
#print("freq of digits of random num generated is \n",d2)

#Generates an excel sheet containing Frequency Distribution Table for Random numbers unit digits
def GenerateFreqTable(digit,unitDigits):
    freq=np.zeros((len(digit),),dtype='int')
    for i in range(0,len(unitDigits)):
        for j in range(0,len(digit)):
            if unitDigits[i]==digit[j]:
                c=j
                freq[c]+=1
    freq_random=pd.DataFrame({"Digit":digit,"Frequency":freq,"Probability":freq/sample_size})
    filepath = 'Freq_Table_generated_random.xlsx'
    freq_random.to_excel(filepath,'sheet_random',index=False)
    return;

GenerateFreqTable(digit,unitDigits)

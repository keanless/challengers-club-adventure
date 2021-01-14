import math
import os
import random
import re
import sys


def plusMinus(arr):
    
    postive = 0 
    negative = 0
    zero = 0
    for i in range (len(arr)):
        if arr[i]>0 :
            
            postive += 1
        elif arr[i]<0:
          negative += 1
        else : 
            zero += 1
            
    print(postive/len(arr))     
    print(negative/len(arr))  
    print(zero/len(arr))      
    
        
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
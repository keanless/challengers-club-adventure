import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
            for x in range (n):
                if i+x == n-1:
                    print(" "*x+"#"*(n-x))
    
    

if __name__ == '__main__':
    n = int(input())

    staircase(n)

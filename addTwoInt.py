#!/usr/bin/env python3
 
import sys

print(sys.argv)

a=int(sys.argv[1])
b=int(sys.argv[2])

def add(a,b):
  sum=a+b
  return sum 


print("The sum of the two values is: ",add(a,b))

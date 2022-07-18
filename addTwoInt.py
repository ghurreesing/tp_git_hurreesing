#!/usr/bin/env python3
 
import sys

if len(sys.argv) == 1:
  print ('Error No arguments entered: Provide two arguments')
  sys.exit()

if len(sys.argv) == 2:
  print ('Error one argument entered: Provide two arguments')
  sys.exit()

if len(sys.argv) >= 4:
  print ('Error more than two  arguments entered: Provide only two arguments')
  sys.exit()


print(sys.argv)

a=int(sys.argv[1])
b=int(sys.argv[2])


def add(a,b):
  sum=a+b
  return sum 

print("The sum of the two values is: ",add(a,b))



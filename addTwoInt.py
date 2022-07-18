#!/usr/bin/env python3
 
import sys

if len(sys.argv) == 1:
  print ('Error No arguments entered: Provide two arguments')
  a=int(input("Enter a number: "))
  b=int(input("Enter a number: "))

if len(sys.argv) == 2:
  print ('Error one argument entered: Provide two arguments')
  a=int(sys.argv[1])
  b=int(input("Enter a number: "))

if len(sys.argv) == 3:
   a=int(sys.argv[1])
   b=int(sys.argv[2])

if len(sys.argv) >= 4:
  print ('Error more than two  arguments entered: Provide only two arguments')
  a=int(input("Enter a number: "))
  b=int(input("Enter a number: "))



def add(a,b):
  sum=a+b
  return sum 

print("The sum of the two values", a, "and", b,"is: ",add(a,b))



 
import math 
MAX = 1000000 
  
# Function to return  
# the nth Fibonacci number  
def fib(n):  
  
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5)) 
   
  
# Function to return  
# the required sum of the array  
def calculateSum(l, r): 
  
    # Using our deduced result  
    sum = fib(r + 2) - fib(l + 1) 
  
    return sum
  
# Function to return the sum of  
# fibonacci in the Kth array  
def sumFibonacci(k) : 
    # Count of fibonacci which are in  
    # the arrays from 1 to k - 1  
    l = (k * (k - 1)) / 2
    r = l + k 
  
    sum = calculateSum(l, r - 1)  
  
    return sum
  
# Driver code  
k = 3 
  
print(sumFibonacci(k)) 
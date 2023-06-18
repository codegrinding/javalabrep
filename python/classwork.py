'''# addition of two number
a=5
b=6
c=a+b
print("the sum of {1} and {2} is {3}".format(a,b,c))
'''


'''
# check for prime number
 num = int(input("Enter a number: "))

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")       

else:
   print(num,"is not a prime number")

'''
'''
# simple calculator
def add(x, y):
   return x + y 
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
'''

'''
#  find the factorial of number
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
'''


'''
#  calculate the square root


num = float(input('Enter a number: '))
sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,sqrt))
'''

'''
#  find the area of triangle

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
'''

'''
 a = float(input('Enter a: '))
 b = float(input('Enter b: '))
 c = float(input('Enter c: '))
 d = (b**2) - (4*a*c)
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(s1,s2))
'''

'''
#  swap two variables
x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
'''

'''
#  generate a random number between 0 and 9
import random
print(random.randint(0,9))
'''

'''
km = input("Enter value in km")
conv_fac = 0.621
miles = km * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(km,miles))
'''

'''
#  convert temperature in celsius to fahrenheit

c = 37.5
f = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(f,c))
'''

'''
# check wether number is positve negative or zero
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
'''

'''
# check the number wehter it is odd or even
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
'''

'''
# check if the input year is a leap year or not
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
'''

'''
# find the largest number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number between",num1,",",num2,"and",num3,"is",largest)
'''


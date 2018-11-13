# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 01:28:23 2018

@author: aneta sokolowska
@student number: 10379935
"""
############################################################################################
# CA5 Python Calculator with Lambda, Map, Filter, Reduce etc... - 10% Assignment
# This CA involves modifying your calculator class from CA1 
# to ensure that it can handle lists of data.
# You will be required to refactor / rewrite your functions so that they can handle lists.
# You will need to use:
# 1. lambda (add,cube,divide,exponent,square)
# 2. map (add,cube,divide,exponent,square)
# 3. filter (sqrt)
# 4. reduce (factorial)
# 5. generator(sum)
# 6. list comprehension (add,cube,divide,exponent,multiply,sinus)
#in any manner you deem necessary to achieve this
# Submit a Python script of your program to moodle and github as well as any tests you have
# done which should still work.
############################################################################################

import math 
# Importing math library to be able to use the following functions:
# factorial,sinus,square root.

from functools import reduce
# Importing reduce from functools as this is Python3 requirement,
#if it was Python2 this would not be needed
import operator  
#Importing operator to use it for the factorial function

# In Python 3 there are three distinct numeric types: plain integers int(), 
# floating point numbers float(), and complex numbers complex().For the purpose 
# of this exercise I will only use float and integer number.
# isinstance check the type of number

class Calculator(object): 
              
    def add(self,x,y):
        number_types=(int,float) 
        #using list comprehension to check what type of numbers are in the list
        #as per definition: [ expression for item in list if conditional ]
        #Expression is based on the variable used for each element in the list
        #To raise error if the lists are not the same lenght or if the values are not valid
        if [i for i in x if not isinstance(i,number_types)] or [i for i in y if not isinstance(i,number_types)] or (len(x) !=len(y)):
            return('You have either input incorrect number or the lists are not the same length')
        else:
            return (list(map(lambda x, y: x+y, x, y)))

    def cube(self,x):
        number_types=(int,float)
        if [i for i in x if not isinstance(i,number_types)]:
            return ('You have entered not a valid number, please choose either integer or float') 
        else:
            return (list(map(lambda x: x*x*x, x)))
            
    def divide(self,x,y):
        number_types=(int,float)
        #To raise error if the lists are not the same lenght or if the values are not valid
        if [i for i in x if not isinstance(i,number_types)] or [i for i in y if not isinstance(i,number_types)] or (len(x) !=len(y)):
            return('You have either input incorrect number or the lists are not the same length')
        #This is to raise division by zero error, if any item in y list has zero in it
        #the below error will appear
        if [i for i in y if i== 0]:
            return('Division by zero is not allowed')  
        #The below is to raise error if lists are not the same length)
        else:
            return (list(map(lambda x, y: x/y, x, y)))
                   
    def exponent(self,x,y):
        number_types=(int,float)
        #To raise error if the lists are not the same lenght or if the values are not valid
        if [i for i in x if not isinstance(i,number_types)] or [i for i in y if not isinstance(i,number_types)] or (len(x) !=len(y)):
            return('You have either input incorrect number or the lists are not the same length')
        #The below is to raise error if lists are not the same length
        if(len(x) != len(y)):
            return ('The lists are not the same length')
        else:
            return (list(map(lambda x, y: x**y, x, y)))
            
        
    def factorial(self,x):
        if not isinstance(x, int) or x <= 0:
            return ('Your input is incorrect')
        else:
            return reduce(operator.mul, range(1, x+1), 1)
            
    def multiply(self,x,y):
        number_types=(int,float)
        #To raise error if the lists are not the same lenght or if the values are not valid
        if [i for i in x if not isinstance(i,number_types)] or [i for i in y if not isinstance(i,number_types)] or (len(x) !=len(y)):
            return('You have either input incorrect number or the lists are not the same length')
        else:
            return (list(map(lambda x, y: x*y, x, y)))
            
    def sinus(self,x):
        number_types=(int,float)
        #To raise error if the lists are not the same lenght or if the values are not valid
        if [i for i in x if not isinstance(i,number_types)]:
            return ('You have not entered a valid number')
        else:
            return (list(map(lambda x: math.sin(x), x)))
       
         
    def square(self,x):
        number_types=(int,float)
        if [i for i in x if not isinstance(i,number_types)]:
            return ('You have entered not a valid number') 
        else:
            return (list(map(lambda x: x**2, x)))
        
    def sqrt(self,x):
            if (list(filter(lambda x: x>0, x))):
                return (list(map(lambda x: math.sqrt(x), x)))
            else:
                return('Your input is incorrect')
            
    def substract(self,x,y):
        number_types=(int,float) 
        if [i for i in x if not isinstance(i,number_types)] or [i for i in y if not isinstance(i,number_types)] or (len(x) !=len(y)):
            return('You have either input incorrect number or the lists are not the same length')
        else:
            return (list(map(lambda x, y: x-y, x, y)))
        

   #Generator  will sum all of the numbers starting from zero, adding 4 and will finish at 400
    def sum_generator(start=0, end=400, step=4):
        while True:
            yield start
            start+=step
            if start>=end: 
                break


    sum=sum_generator()
    next(sum)
    





  
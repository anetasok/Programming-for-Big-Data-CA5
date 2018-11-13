# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 01:27:19 2018

@author: aneta sokolowska
@student number: 10379935

"""

import unittest

from CA5 import Calculator
# Testing the functionality of the Calculator.
# Our Calculator will have the following functions:
# 1.Add
# 2.Cube
# 3.Divide
# 4.Exponent
# 5.Factorial
# 6.Multiply
# 7.Sinus
# 8.Square
# 9.Square root
# 10.Substarct


class CalculatorTest(unittest.TestCase):
# Adding new setUp function to make the tests shorter, otherwise there will be a lot of repeats. 
# The test runner will run this method prior each test.
    
    def setUp(self): 
        self.calc=Calculator()
        
# The test functions must start with test otherwise they will not run.
# 1. Add is the first function to be tested.
        
    def testAdd(self): 
        result = self.calc.add([2,4,6,8],[1,3,5,7]) 
        self.assertEqual([3,7,11,15],result) 
        result = self.calc.add([2,3,4],[1,2,4])
        self.assertEqual([3,5,8],result)
        result = self.calc.add([1.2,2.3,9],[-2,-3.4,-11])
        self.assertEqual([-0.8, -1.1, -2],result) 
        result=self.calc.add([22,41,16,8,-5],[1,'p',5,7])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result) 

# 2.Tesing function Cube.
        
    def testCube(self):
        result=self.calc.cube([1,2])
        self.assertEqual([1,8],result) 
        result=self.calc.cube([-2,1.2,0,6])
        self.assertEqual([-8,1.728,0,216],result)
        result=self.calc.cube([1])
        self.assertEqual([1],result)

# 3. Testing function Divide.
    
    def testDivide(self):
        result=self.calc.divide([4,10,30],[2,5,2])
        self.assertEqual([2,2,15],result)
        result=self.calc.divide([4,10,30],[0,5,0])
        self.assertEqual('Division by zero is not allowed',result)
        result=self.calc.divide([4,8,10,30],[1,7,2])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result) 
        result=self.calc.divide(['e',8,10,30],[1,7,'t',1,'z'])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result)
     
# 4. Testing function Exponent.
        
    def testExponent(self):
        result=self.calc.exponent([0,1,2,-3],[0,1,2,3]) 
        self.assertEqual([1,1,4,-27],result) 
        result=self.calc.exponent([0,1,2],[0,1,2,3])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result) 
        result=self.calc.exponent([2,9],[2,'r'])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result) 
        
# 5. Testing factorial function.
        
    def testFactorial(self):
        result=self.calc.factorial(5)
        self.assertEqual(120,result) 
        result=self.calc.factorial(-5)
        self.assertEqual('Your input is incorrect',result) 
        result=self.calc.factorial(0.8)
        self.assertEqual('Your input is incorrect',result) 
     
# 6. Testing Multiply function.
        
    def testMultiply(self):
        result=self.calc.multiply([0,1,-2,0.5],[0,1,2,3])
        self.assertEqual([0,1,-4,1.5],result)
        result=self.calc.multiply([0,1,-2,'i'],[0,1,2,3])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result)
        result=self.calc.multiply([0,1,-2,0.5],[0,3])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result)
        

# 7. Testing Sinus function
       
    def testSinus(self):
        result=self.calc.sinus([1,2,3,'r'])
        self.assertEqual('You have not entered a valid number',result)
        result=self.calc.sinus([1,2,3])
        self.assertEqual([0.8414709848078965, 0.9092974268256817, 0.1411200080598672],result)
        result=self.calc.sinus([0.7])
        self.assertEqual([0.644217687237691],result)

# 8.Testing Square function.
        
    def testSquare(self):
        result=self.calc.square([9,6,-5,3.5,0])
        self.assertEqual([81,36,25,12.25,0],result)
        result=self.calc.square([3,'t'])
        self.assertEqual('You have entered not a valid number',result)
        
# 9.Testing Square Root function.
        
    def testSqrt(self):
        result=self.calc.sqrt([25,9])
        self.assertEqual([5,3],result)
        result=self.calc.sqrt([-8,0])
        self.assertEqual('Your input is incorrect',result)

 
# 10.Testing Substract function.
        
    def testSubstract(self):
        result=self.calc.substract([30,-12],[2,4])
        self.assertEqual([28,-16],result)
        result=self.calc.substract([-22,-28],['s','o','s'])
        self.assertEqual('You have either input incorrect number or the lists are not the same length',result)
            
 #For the generator test to work you have to run the actual generator first:
 #Please run the below code for sum_generator and then run the test again
 
    def sum_generator(start=0, end=400, step=4):
        while True:
            yield start
            start+=step
            if start>=end: 
                break


    sum=sum_generator()
    next(sum)
    
    def testSumGenerator(self):
        sum=sum_generator(0)
        self.assertEqual(0,next(sum))
        self.assertEqual(4,next(sum))
        self.assertEqual(8,next(sum))
        self.assertEqual(12,next(sum))
        
        
if __name__ == '__main__':
    unittest.main()


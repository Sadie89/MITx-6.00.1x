# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:39:57 2020

@author: ghaff
"""

########## edx midterm ##########
# ########## Q1-1 ##########
# x = "pi"
# y = "pie"
# x, y = y, x
# print(y)
# ########## Q1-2 ##########
# def f(x):
#     while x > 3:
#         f(x+1)
# ########## Q1-5 ##########
# i = -1
# j = -1
# while i >= 0:
#     while j >= 0:
#         print(i, j)
# ########## Q2-5 ##########
# L = [1,2,3]
# d = {'a': 'b'}
# def f(x):
#     return 3

# for i in range(10, -1, -2):
#     print(f)
    
# ########## Q2-6 ##########
# stuff = "iQ"
# for thing in stuff:
#         if thing == 'iQ':
#            print("Found it")

# def Square(x):
#     return SquareHelper(abs(x), abs(x))

# def SquareHelper(n, x):
#     if n == 0:
#         return 0
#     return SquareHelper(n-1, x) + x
# print(Square(100))

# ########## Q3 ##########
# def evalQuadratic(a, b, c, x):
#    '''
#    a, b, c: numerical values for the coefficients of a quadratic equation
#    x: numerical value at which to evaluate the quadratic.
#    '''
#    return a*x*x + b*x + c

# def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
#     '''
#     a1, b1, c1: one set of coefficients of a quadratic equation
#     a2, b2, c2: another set of coefficients of a quadratic equation
#     x1, x2: values at which to evaluate the quadratics
#     '''
#     # Your code here
#     return (print(evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)))
  
# twoQuadratics(1,0,0,2,1,0,0,3)

# ########## Q4 ##########
# def lessThan4(aList):
#     '''
#     aList: a list of strings
#     returns a sublist of strings (bList) in aList that contain fewer than 4 characters
#     '''
#     # Your code here
#     bList = []
#     for item in aList:
#         if len(item) < 4:
#             bList.append(item)
#     return bList
# aList = ["apple", "cat", "dog", "banana"]
# aList = ["",""]
# print(lessThan4(aList))

########## Q5 ##########
# aDict = {"A": 1, "B": 2, "C":2, "D": 3, "F": 4}
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    
    Returns a list of keys in aDict that map to integer values that are unique 
    '''

    flipped = {} 
    for key, value in aDict.items(): 
        if value not in flipped: 
            flipped[value] = [key] 
        else: 
            flipped[value].append(key) 
    
    result = [key for key, values in flipped.items() if len(values) > 1]
    for item in result:
        aDict = {key:val for key, val in aDict.items() if val != item}
    uniquekey_list = list(aDict.keys())
    uniquekey_list.sort()
    return uniquekey_list

print (uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0}))

# print("duplicate values", result)
# print("type(result):", type(result))
# print("length values", len(result))

# ########## Q6 ##########
# def gcd(a, b):
#     '''
#     a, b: positive integers
    
#     returns: the greatest common divisor of a & b.
#     '''
#     # Your code here
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
# print(gcd(0,10))

# ########## Q7 ##########
# def score(word, f):
#     """
#        word, a string of length > 1 of alphabetical 
#              characters (upper and lowercase)
#        f, a function that takes in two int arguments and returns an int

#        Returns the score of word as defined by the method:

#     1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
#        times its distance from start of word.  
#        Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
#     2) The score for a word is the result of applying f to the
#        scores of the word's two highest scoring letters. 
#        The first parameter to f is the highest letter score, 
#        and the second parameter is the second highest letter score.
#        Ex. If f returns the sum of its arguments, then the 
#            score for 'adD' is 12 
#     """
#     i = 0
#     scores = []
#     for char in word.lower():
#         score = (ord(char) - 96) * i
#         scores.append(score)
#         i += 1
#     sorted_scores = sorted(scores)
#     return f(sorted_scores[-1], sorted_scores[-2])
       

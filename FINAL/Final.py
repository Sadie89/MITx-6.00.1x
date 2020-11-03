# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:53:38 2020

@author: ghaff
"""

######### EDX: MIT 6001x Final Exam ##########

# ######### Problem 3: Palindrome ##########

# '''
# Write a Python function that returns True if aString is a palindrome 
# (reads the same forwards or reversed) and False otherwise.
# Do not use Python's built-in reverse function or aString[::-1] to reverse strings.
# This function takes in a string and returns a boolean.
# '''

# def isPalindrome(aString):
#     '''
#     aString: a string
#     Returns True is aString is Palindrome
#     '''
#     if len(aString) == 0 or len(aString) == 1:
#         return True
#     else:
#         for i in range(len(aString)):
#             if aString[i] != aString[- i - 1]:
#                 return False
#             else:
#                 Flag = 1
#     if Flag == 1:
#         return True
    

# # aString = ""
# # aString = " "
# # aString = " 1"
# # aString = "  "
# # aString = "1"
# # aString = "a"
# # aString = "11"
# # aString = "aa"
# # aString = "121"
# # aString = "aba"
# # aString = "1221"
# # aString = "1231"
# # aString = "12344321"
# # aString = "1234321"
# aString = "12345321"

# print (isPalindrome(aString))


# ######### Problem 4: Prime Number List ##########
# '''
# Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. 
# A prime number is a number that is divisible only by 1 and itself. 
# This function takes in an integer and returns a list of integers.
# '''

# def primes_list(N):
#     '''
#     N: an integer
#     Returns a list of prime numbers between 2 and N
#     '''
#     primeList = []
#     firstPrime = 2
#     primeFlag = 0
#     i = firstPrime
#     while i <= N:
#         if primeList == []:
#             primeList.append(firstPrime)
#         else:
#             for p in primeList:
#                 if (i % p) != 0:
#                     primeFlag += 1
                
#             if primeFlag == len(primeList):
#                 primeList.append(i)
#                 primeFlag = 0
#             else:
#                 primeFlag = 0
#         i += 1    
#     return primeList

# # prime_list = primes_list(0)
# # prime_list = primes_list(1)
# # prime_list = primes_list(2)
# # prime_list = primes_list(3)
# # prime_list = primes_list(4)
# # prime_list = primes_list(5)
# # prime_list = primes_list(11)
# # prime_list = primes_list(12)


# print(prime_list)


# ######### Problem 5: dictionary intersect difference ##########
# '''
# Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.

# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
# Here are two examples:

# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
# '''

# def dict_interdiff(d1, d2):
#     '''
#     d1, d2: dicts whose keys and values are integers
#     Returns a tuple of dictionaries according to the instructions above
#     '''
#     intersectDict = {}
#     differenceDict = {}
#     for key in d1.keys():
#         if key in d2.keys():
#             val = f(d1[key], d2[key])
#             intersectDict[key] = val
#             # intersectDict[key] = "intersect"
#         else:
#             differenceDict[key] = d1[key]
#     for key in d2.keys():
#         if key not in d1.keys():
#             differenceDict[key] = d2[key]
        
#     return intersectDict, differenceDict
    

# def f(a,b):
#     '''
    
#     Parameters
#     ----------
#     a : TYPE
#         integer.
#     b : TYPE
#         integer.
    
#     Performs a random operation on a and b
#     Returns the results, could be integer or boolean
#     -------
#     answer : TYPE
#         integer or boolean.

#     '''
#     import operator
#     import random
    
#     op_mappings = {"+":  operator.add,
#                    "-":  operator.sub,
#                    "*":  operator.mul,
#                    "/":  operator.truediv,
#                    "<":  operator.lt,
#                    ">":  operator.gt,
#                    "==":  operator.eq,
#                    "<=": operator.le}
    
#     op = random.choice(["+", "-", "*", "/","<",">","==","<="])
#     #print(op)
#     answer = op_mappings[op](a, b)
#     # answer = a + b
#     return answer
    
# # print(f(2,3))

# # d1 = {}
# # d2 = {}

# # d1 = {1:30, 2:20, 3:30}
# # d2 = {1:40, 2:50, 3:60}

# # d1 = {1:30, 2:20, 3:30, 5:80}
# # d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

# # d1 = {1:20, 2:30, 4:50}
# # d2 = {1:20, 2:30, 4:50}

# # d1 = {1:20, 2:30, 4:50}
# # d2 = {}

# # d1 = {1:20, 2:30, 4:50}
# # d2 = {1:[10, 30]}

# print(dict_interdiff(d1, d2))

# ######### Problem 6: Class Infinite Loop Issue ##########

# class Person(object):     
#     def __init__(self, name):         
#         self.name = name     
#     def say(self, stuff):         
#         return self.name + ' says: ' + stuff     
#     def __str__(self):         
#         return self.name  

# class Lecturer(Person):     
#     def lecture(self, stuff):         
#         return 'I believe that ' + Person.say(self, stuff)  

# class Professor(Lecturer): 
#     def say(self, stuff): 
#         return self.name + ' says: ' + self.lecture(stuff)

# class ArrogantProfessor(Professor): 
#     def say(self, stuff): 
#         return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
#     def lecture(self, stuff): 
#         return 'It is obvious that ' + Person.say(self, stuff)

# e = Person('eric') 
# le = Lecturer('eric') 
# pe = Professor('eric') 
# ae = ArrogantProfessor('eric')
# print(e.say('the sky is blue'))
# print(le.say('the sky is blue'))
# print(le.lecture('the sky is blue'))
# print(pe.say('the sky is blue'))
# print(pe.lecture('the sky is blue'))
# print(ae.say('the sky is blue'))
# print(ae.lecture('the sky is blue'))


######### Problem 7: MIT Campus Class Implementation##########
### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)

class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.campus = []
        self.campus.append(self.tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Location.dist_from(self.tent_loc, self.new_tent_loc)
        for item in self.campus:
            if Location.__eq__(item, new_tent_loc) == True:
                return False
            elif Location.dist_from(item, new_tent_loc) < 0.5:   
                return False
        self.campus.append(new_tent_loc)
        return True
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        try:
            self.campus.remove(tent_loc)
        except ValueError:
            raise ValueError
                
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        CampusLocation = []
        for item in self.campus:
            CampusLocation.append(Location.__str__(item))
        return sorted(CampusLocation)

# c = MITCampus(Location(1,2))
# print(c.add_tent(Location(2,3))) # should return True
# print(c.add_tent(Location(1,2))) # should return True
# print(c.add_tent(Location(0,0))) # should return False
# print(c.add_tent(Location(2,3))) # should return False
# print(c.get_tents()) # should return ['<0,0>', '<1,2>', '<2,3>']
# print(c.remove_tent(Location(1,2)))
# print(c.get_tents())
# print(c.remove_tent(Location(10,10)))



c = MITCampus(Location(1,2), Location(0,1))
c.add_tent(Location(-1,2))
c.add_tent(Location(1,-10))
c.add_tent(Location(1,10))
c.add_tent(Location(1,20))
c.add_tent(Location(1,40))
print(sorted(c.get_tents()))
# print(check_if_x_sorted(c.get_tents()))
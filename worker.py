#!/bin/python3

from stringlib import *

#Add a Worker class to this file.
class worker:
#The Worker class constructor needs to take as input
#a string.  It will set its own data member to that string.
    # inputStr = ""
    def __init__(self, s):
        self.inputStr = s
#Add methods to the Worker class that are equivalent to
#functions in the stringlib module.  These methods will
#not take a string as input (except for the containsWord
#method, which will take the contained string parameter).  Instead,
#these methods will operate on the Worker class data member. 
#Your method can call the needed function in the stringlib
#module.

#reverseStr - takes as input a string and returns the reverse of it
    def wreverseStr(self):
        reverseS = self.inputStr [::-1] #this creates a slice that starts at the end of the string and moves backwards
        return reverseS
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
    def wcontainsWord(self, containedStr):
        if containedStr in self.inputStr:
            return "Yes"
        else:
            return "No"
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
    def wisPalindrome(self):
        reverseS = self.inputStr [::-1]
        if reverseS == self.inputStr:
            return "Yes"
        else:
            return "No"
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
    def wupperCaseStr(self):
        return self.inputStr.upper()


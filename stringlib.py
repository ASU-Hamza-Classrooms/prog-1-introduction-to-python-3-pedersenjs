#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
def reverseStr(s):
    reverseS = s [::-1] #this creates a slice that starts at the end of the string and moves backwards
    return reverseS
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
def containsWord(containingStr, containedStr):
    if containedStr in containingStr:
        return "Yes"
    else:
        return "No"
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
def isPalindrome(s):
    reverseS = s [::-1]
    if reverseS == s:
        return "Yes"
    else:
        return "No"
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
def upperCaseStr(s):
    return s.upper()


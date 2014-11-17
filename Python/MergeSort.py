#! /usr/bin/python2.7
"""
#=============================================================================#

FILE            : MergeSort.py 

DESCRIPTION     : Implementation of Recursive MergeSort in Python

COMPLEXITY      : O(nlogn)
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 13 23:34:22 CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import random

def MergeSort ( slist ):

    if len ( slist ) > 1:

        mid = len (slist)/2
        lpart = slist[:mid]
        rpart = slist[mid:]

        MergeSort (lpart)
        MergeSort (rpart)
   
        i = 0
        j = 0
        c = 0

        while i < len(lpart) and j < len(rpart):
            if lpart[i] < rpart[j]:
                slist[c] = lpart[i]
                i = i + 1
            else:
                slist[c] = rpart[j]
                j = j + 1
            c += 1

        while i < len(lpart) and j == len(rpart):
            slist[c] = lpart[i]
            i = i + 1
            c = c + 1
        while j < len(rpart) and i == len(lpart):
            slist[c] = rpart[j]
            j = j + 1
            c = c + 1
    return slist

# better replace with random generated array
slist = [ random.randint(0, 100) for c in range(10) ]
print MergeSort (slist)


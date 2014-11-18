#! /usr/bin/python2.7
"""
#=============================================================================#

FILE            : BubbleSort.py 

DESCRIPTION     : Implementation of the Elementary sorting algorithm  
                  Bubble Sort in Python

COMPLEXITY      : O(n^2)
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 17 #:#:# CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""

def BubbleSort (slist):

    for i in range (len(slist)):
        for j in range ( len(slist) -i ):


slist = [ random.randint(0, 100) for c in range(10) ]
print BubbleSort (slist)

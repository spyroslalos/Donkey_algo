#! /usr/bin/python2.7
"""
#=============================================================================#

FILE            : InsertionSort.py 

DESCRIPTION     : Implementation of Insertion Sort in Python

COMPLEXITY      : Best O(n) | Average O(n^2) | Worst O(n^2)
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 08 22:42:26 CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""

def InsertionSort( mlist ):
	
    for i in range( 1, len( mlist ) ):
	tmp = mlist[i]
        j = i
        while j > 0 and tmp < mlist[j - 1]:
            mlist[j] = mlist[j - 1]
            j -= 1
        mlist[j] = tmp
    print mlist

list = [4, 3, 7, 13, 2, 32, 6, 1, 1, 24]
InsertionSort( list )

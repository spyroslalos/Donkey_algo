#! /usr/bin/python2.7

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

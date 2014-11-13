#! /usr/bin/python2.7

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

slist = [34,12,2,7,27,1,11,3]
MergeSort (slist)
print slist

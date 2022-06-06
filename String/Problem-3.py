import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


# Find Duplicates in String 
# string = "test string"
# s, count = 2 
# t, count = 3 


s='test string'


def duplicatesOfString(s):
    countDict={}
    duplicates=[]
    for i in s:
        if(i not in countDict):
            countDict[i]=1
        else:
            countDict[i]+=1
            if(i not in duplicates): 
                duplicates.append(i)
    for i in duplicates:
        print(i,"->",countDict[i])

duplicatesOfString(s)
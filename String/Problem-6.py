import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Write a Program to check whether a string 
# is a valid shuffle of two strings or not

# str1 = 'onetwofour'
# str2 = 'hellofourtwooneworld'

# Output : 1

# s1 = 'onetwofour'
# s2 = 'hellofourtwooneworld'


s1 = 'yellow'
s2 = 'yellowsssssssssssssss'


#Solution 1 : Using Sliding window technique(Indexing) + Sort

# def checkifStringOneisShuffledSubStringOfStringTwo(s1,s2):
#     m=len(s1)
#     n=len(s2)

#     if(m>n):
#         return 0
#     s1=sorted(s1)
#     for i in range(n-m+1):
#         curString=s2[i:i+m]
#         curString=sorted(curString)
#         if(s1==curString):
#             return 1
#     return 0


#Solution 2 : Using sliding window and dictionary

def createCountDict(s):
    d={}
    for i in s:
        if(i not in d):
            d[i]=1
        else:
            d[i]+=1
    return d

def checkifStringOneisShuffledSubStringOfStringTwo(s1,s2):
    m=len(s1)
    n=len(s2)

    if(m>n):
        return 0
    s1=sorted(s1)
    s1Dict=createCountDict(s1)
    
    tempS2=s2[:m]
    s2Dict=createCountDict(tempS2)
    if(s2Dict==s1Dict):
        return 1
    else:
        start=1
        while(start<n-m+1):
            curString=s2[start:start+m]
            curStringdict=createCountDict(curString)
            if(s1Dict==curStringdict):
                return 1
            start+=1
        return 0


print(checkifStringOneisShuffledSubStringOfStringTwo(s1, s2))

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# A Program to check if strings are rotations of each other or not
# Input:
# string1 = "AACD"
# string2 = "ACDA"
# Output : 1


# s1 = "ABCD"
# s2 = "CDAB"

s1 = "ABCD"
s2 = "ACBD"


#Solution 1 : 
#Take temporary string and add string1 2 times to it
#Then check whether string2 is substring of tempString
#if yes then return 1 
#else return 0


# def checkIfStringsAreRotation(s1,s2):
#     temp=s1+s1
#     if(temp.count(s2)>0):
#         return 1
#     return 0



#Solution 2 :
#1.take two array one for string1 and second for string2
#2.remove first index of string2 and append at last to it
#3.check if two strings are equal at this stage
#4.if yes return 1 else return 0
#Repeat step 2,3,4 for length of string2



def checkIfStringsAreRotation(s1,s2):
    s1=list(s1)
    s2=list(s2)
    if(len(s1)!=len(s2)):
        return 0
    for i in range(len(s2)):
        cur=s2[0]
        s2.pop(0)
        s2.append(cur)
        if(s1==s2):
            return 1
    return 0

print(checkIfStringsAreRotation(s1, s2))








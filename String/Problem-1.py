import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

#Reverse a string
# Input:
# s = Geeks
# Output: skeeG



s="geeks"

# def reverseString(s):
#     return s[::-1]

# def reverseString(s):
#     s.reverse()
#     return s 

def reverseString(s):
    n=len(s)
    start=0
    end=n-1
    s=list(s)
    while(start<end):
        #swap start and end
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    
    return "".join(s)

print(reverseString(s))

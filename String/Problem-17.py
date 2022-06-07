import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Word Break Problem

# Given an input string and a dictionary of words,
#  find out if the input string can be segmented into 
# a space-separated sequence of dictionary words. 
# See following examples for more details. 

# Consider the following dictionary 
# { i, like, sam, sung, samsung, mobile, ice, 
#   cream, icecream, man, go, mango}

# Input:  ilike
# Output: Yes 
# The string can be segmented as "i like".

# Input:  ilikesamsung
# Output: Yes
# The string can be segmented as "i like samsung" 
# or "i like sam sung".


dictionary={ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i","like", "ice", "cream" }
s="imobilelike"



#Solution 1 : Using Recusing

# def wordBreak(s,dictionary):
#     if(len(s)==0):
#         return True 
#     else:
#         wordlen=len(s)
#         for i in range(1,wordlen+1):
#             if(s[:i] in dictionary and wordBreak(s[i:], dictionary)):
#                 return True 
#         return False 


#Solution 2 : Using DP

def wordBreak(s,dictionary):
    n=len(s)
    dp=[False for i in range(n+1)]

    dp[0]=True

    for i in range(n+1):
        for j in range(i):
            if(dp[j] and s[j:i] in dictionary):
                dp[i]=True
                break 
    
    print(dp)

    return dp[n]


print(wordBreak(s,  dictionary))

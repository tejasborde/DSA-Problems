import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')

# Edit Distance 
# Given two strings s and t. Return the minimum number of operations required to convert s to t.
# The possible operations are permitted:

# Insert a character at any position of the string.
# Remove any character from the string.
# Replace any character from the string with any other character.

# Input: 
# s = "geek", t = "gesek"
# Output: 1
# Explanation: One operation is required 
# inserting 's' between two 'e's of str1.


s1 = "sunday"
s2 = "saturday"





def editDistanceTomakeBothStringsSame(s1,s2):
    m=len(s1)
    n=len(s2)
    
    if(m==0):
        return n 
    
    if(n==0):
        return m 
    

    dp=[[0 for i in range(n+1)]for j in range(m+1)]


    for i in range(m+1):
        for j in range(n+1):
            if(i==0):
                dp[i][j]=j
            elif(j==0):
                dp[i][j]=i 
            elif(s1[i-1]==s2[j-1]):    #If last chars are same of both string
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1], #For insert
                            dp[i-1][j],    #For remove
                            dp[i-1][j-1])  #For replace
    
    return dp[m][n]


print(editDistanceTomakeBothStringsSame(s1, s2))
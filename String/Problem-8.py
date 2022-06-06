import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')






# Longest Palindrome SubString 
# Input:
# S = "aaaabbaa"
# Output: aabbaa
# Explanation: The longest Palindromic
# substring is "aabbaa".

# S = "forgeeksskeegfor"
# S = "geeks"
S = "o"


#Solution 1 : Bruteforce O(n^3)
#Generate all substrings

# def longestPalindromeSubString(S):
#     n=len(S)
#     maxLength=float('-inf')
#     maxPal=None
#     for i in range(n):
#         for j in range(i,n):
#             curString=S[i:j+1]
#             if(curString==curString[::-1] and len(curString)>maxLength):
#                 maxLength=len(curString)
#                 maxPal=curString
#     print(maxPal)
#     return maxLength



#========================================================
#Solution 2 : Using dynamic Programming

# def longestPalindromeSubString(S):
#     n=len(S)
#     maxLength=1
#     maxPal=None

#     mat=[[0 for i in range(n)] for j in range(n)]

#     #all strings with length one will be palindrome
#     for i in range(n):
#         mat[i][i]=1
    
 
#     #check all strings with length two 
#     for i in range(n-1):
#         if(S[i]==S[i+1]):
#             mat[i][i+1]=1
#             maxLength=2
#             maxPal=S[i:i+2]
    
#     k=3

#     while(k<=n):
#         i=0
#         while(i<n-k+1):
#             j=i+k-1
#             #String is palindrome if its last and first char is same and middle string is palindrome
#             if(mat[i+1][j-1]==1 and S[i]==S[j]):
#                 mat[i][j]=1

#                 if(k>maxLength):
#                     maxLength=k 
#                     maxPal=S[i:j+1]
#             i+=1
#         k+=1
#     # print(maxLength)
#     return maxPal
        

#========================================================
#Solution 3 : O(n^2)
#Iterate over the string and for each char 
#traverse towards left and right till both positions are having same chars

def longestPalindromeSubString(S):
    n=len(S)
    if(n<2):
        return S
    
    start=0
    maxLength=1
    maxPal=S[0]

    for i in range(n):
        low=i-1
        high=i+1

        while(high<n and S[high]==S[i]):
            high+=1

        while(low>=0 and S[low]==S[i]):
            low-=1

        while(high<n and low>=0 and  S[high]==S[low]):
            high+=1
            low-=1
        
        length=high-low-1

        if(length>maxLength):
            maxLength=length
            start=low+1
            maxPal=S[start:start+maxLength]
    return maxPal
        

print(longestPalindromeSubString(S))


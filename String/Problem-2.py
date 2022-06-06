import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Check if String is Palindrome
# Input: S = "abba"
# Output: 1
# Explanation: S is a palindrome



S='abba'

#Solution 1 : reversing the String

# def isPalindrome( S):
#     if(S==S[::-1]):
#         return 1
#     return 0


#============================================================

#Solution 2 : comparing elements from start and end

def isPalindrome(S):
    n=len(S)
    start=0
    end=n-1

    while(start<end):
        if(S[start]!=S[end]):
            return 0
        start+=1
        end-=1
    return 1


print(isPalindrome( S))
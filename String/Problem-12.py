import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Split the binary string into 
# substrings with equal number of 0s and 1s


# Input: str = “0100110101” 
# Output: 4 
# The required substrings are “01”, “0011”, “01” and “01”.
# Input: str = “0111100010” 
# Output: 3 

# Input: str = “0000000000” 

# Output: -1
 
s='001110010'

def balancedSubstrings(s):

    n=len(s)
    zeroCount=0
    oneCount=0

    count=0
    for i in range(n):
        if(s[i]=='0'):
            zeroCount+=1
        else:
            oneCount+=1
        
        if(oneCount==zeroCount):
            count+=1
    if(oneCount!=zeroCount):
        return -1
    return count
print(balancedSubstrings(s))



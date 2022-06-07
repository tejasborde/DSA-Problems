import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Permutations of a given string 
# Input: ABC
# Output:
# ABC ACB BAC BCA CAB CBA
# Explanation:
# Given string ABC has permutations in 6 
# forms as ABC, ACB, BAC, BCA, CAB and CBA .


s='abc'

def allStrings(s,ans,index):
    if(index==len(s)):
        ans.add("".join(s))
        return 

    for j in range(index,len(s)):
        s[j],s[index]=s[index],s[j]
        allStrings(s,ans,index+1)
        s[j],s[index]=s[index],s[j]
        
ans=set()
S=list(s)
allStrings(S,ans,0)
ans=list(ans)
ans.sort()
print(ans)

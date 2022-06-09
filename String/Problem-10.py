import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Print all subsequences of a string
# Input : abc
# Output : a, b, c, ab, bc, ac, abc

# Input : aaa
# Output : a, aa, aaa

s='abcd'

def printSubSequence(inp,output,ans):
    if(len(inp)==0):
        ans.append(output)
        return
    printSubSequence(inp[1:], output+inp[0], ans)
    printSubSequence(inp[1:], output, ans)


def printAllSubsequences(s):
    ans=[]
    printSubSequence(s,"",ans)
    print(ans)


printAllSubsequences(s)

import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# Array Subset of another array
# Input:
# a1[] = {11, 1, 13, 21, 3, 7}
# a2[] = {11, 3, 7, 1}
# Output:
# Yes
# Explanation:
# a2[] is a subset of a1[]


a1=[10, 5, 2, 23, 19]
a2=[19, 5, 3]

def isSubset(a1,a2):
    for x in a2:
        if(x not in a1):
            return False 
    return True


print(isSubset(a1, a2))












import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')



# Palindrome check
# Example:
# Input:
# 2
# 5
# 111 222 333 444 555
# 3
# 121 131 20

# Output:
# 1
# 0


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))

    ans=1
    for i in arr:
        if(str(i)[::-1]!=str(i)):
            ans=0
            break
    print(ans)







import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')





# Count and Say 
# n=4
# Output : '1211'

n=4

# def sayAndCount(n):
#     if(n==1):
#         return '1'
#     if(n==2):
#         return "11"
    
#     ans="11 "
#     n=n-2
#     while(n!=0):
#         curAns=""
#         l=len(ans)
#         count=1
#         for i in range(1,l):
#             if(ans[i-1]!=ans[i]):
#                 curAns=curAns+str(count)+str(ans[i-1])
#                 count=1
#             else:
#                 count+=1
#         n-=1
#         ans=curAns

#     return ans


#Solution 2 : Using Recursion
def sayAndCount(n):
    ans=""
    if(n==1):
        return "1"
    elif(n==2):
        return "11 "
    else:
        ans=sayAndCount(n-1)+" "
        curAns=""
        l=len(ans)
        count=1
        for i in range(1,l):
            if(ans[i-1]!=ans[i]):
                curAns=curAns+str(count)+str(ans[i-1])
                count=1
            else:
                count+=1
        return curAns
    



print(sayAndCount(n))

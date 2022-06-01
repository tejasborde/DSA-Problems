import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')
m,n=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

def doUnion(a,n,b,m):
    x=list(set(a)|set(b))
    return len(x)

def doIntersection(a,n,b,m):
    x=list(set(a) & set(b))
    return len(x)

def intersect(nums1, nums2):
      m = {}
      if len(nums1)<len(nums2):
         nums1,nums2 = nums2,nums1
      for i in nums1:
         if i not in m:
            m[i] = 1
         else:
            m[i]+=1
      result = []
      print(m)
      for i in nums2:
         if i in m and m[i]:
            m[i]-=1
            result.append(i)
      return result
print(intersect(a, b))
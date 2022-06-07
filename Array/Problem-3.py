import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


#Find the "Kth" max and min element of an array 
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.

arr=[ 7 ,10, 4 ,3, 20 ,15]
n=len(arr)
k=3

#Solution 1 using Sort Function O(nlogn)

# def findKthMin(arr,n,k):
#     arr.sort()
#     return arr[k-1]

# def findKthMax(arr,n,k):
#     arr.sort(reverse=True)
#     return arr[k-1]

# print(findKthMin(arr, n, k))
# print(findKthMax(arr, n, k))


#Solution 2 using heap 
# import heapq
# heapq.heapify(arr)

# ans=None 
# i=1

# while(heapq.heappop(arr)):
#     if(i==k):
#         ans=heapq.heappop(arr)
#         break
#     i+=1
# print(ans)

#Solution 2 using C++ code

#include <iostream>
#include <bits/stdc++.h>
# using namespace std;

# int main()
# {
#     int n=6;
#     int a[6]={7,10,4,3,20,15};
#     int k=3;
    
    
#     //priority_queue<int> p; //3 4 7 10 15 20 gives increasing order queue
#     priority_queue<int,vector<int>,greater<int>> p; // 20 15 10 7 4 3 gives decreasing order queue
    
#     for(int x=0;x<n;x++){
#         p.push(a[x]);
#     }
    
#     int ans,i=1;
    
#     while(!p.empty()){
#         if(i==k){
#             ans=p.top();
#             break;
#         }
#         i++;
        
#         p.pop();
#     }
#     cout<<ans;
    
#     return 0;
# }

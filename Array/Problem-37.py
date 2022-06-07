import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


# https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1
# Largest Rectangular Area in a Histogram
# Input:
# N = 7
# arr[] = {6,2,5,4,5,1,6}
# Output: 12

# arr=[6,2,5,4,5,1,6]
# arr=[7 ,2, 8 ,9 ,1, 3, 6, 5]
arr=[1,2,3,4,5]
n=len(arr)



#Solution 1 : TC- O(n^2)

# class Stack:
#     def __init__(self):
#         self.arr=[]
    
#     def push(self,num):
#         self.arr.append(num)
    
#     def pop(self):
#         x=self.arr.pop()
#         return x 
    
#     def isEmpty(self):
#         if(len(self.arr)==0):
#             return True
#         return False

#     def top(self):
#         return self.arr[-1]

# def findMaxAreaHistogram(arr,n):
#     if(len(arr)==1):
#         return arr[0]
#     left=[0]*n
#     right=[0]*n

#     stack=Stack()

#     for i in range(n):
#         if(stack.isEmpty()):
#             left[i]=0
#             stack.push(i)
#         else:
#             while(stack.isEmpty()==False and arr[stack.top()]>=arr[i]):
#                 stack.pop()
#         if(stack.isEmpty()):
#             left[i]=0
#         else:
#             left[i]=stack.top()+1
#         stack.push(i)

#     while(stack.isEmpty()==False):
#         stack.pop()

#     for i in range(n-1,-1,-1):
#         if(stack.isEmpty()):
#             right[i]=n-1
#             stack.push(i)
#         else:
#             while(stack.isEmpty()==False and arr[stack.top()]>=arr[i]):
#                 stack.pop()
#         if(stack.isEmpty()):
#             right[i]=n-1
#         else:
#             right[i]=stack.top()-1
#         stack.push(i)

#     print(left)
#     print(right)

#     maxArea=0
#     for i in range(n):
#         curArea=(right[i]-left[i]+1)*arr[i]
#         maxArea=max(maxArea,curArea)

#     return maxArea

#===========================================================

#Solution 2 : TC- O(n)

def findMaxAreaHistogram(histogram,n):
    stack = list()

    max_area = 0 # Initialize max area

    # Run through all bars of
    # given histogram
    index = 0
    while index < len(histogram):
        
        # If this bar is higher
        # than the bar on top
        # stack, push it to stack

        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack,
        # then calculate area of rectangle with
        # stack top as the smallest (or minimum
        # height) bar.'i' is 'right index' for
        # the top and element before top in stack
        # is 'left index'
        else:
            # pop the top
            top_of_stack = stack.pop()

            # Calculate the area with
            # histogram[top_of_stack] stack
            # as smallest bar
            area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1)
                if stack else index))

            # update max area, if needed
            max_area = max(max_area, area)
    print(stack)

    # Now pop the remaining bars from
    # stack and calculate area with
    # every popped bar as the smallest bar


    while stack:
        # pop the top
        top_of_stack = stack.pop()

        # Calculate the area with
        # histogram[top_of_stack]
        # stack as smallest bar
        
        area = (histogram[top_of_stack] *
            ((index - stack[-1] - 1)
                if stack else index))

        # update max area, if needed
        max_area = max(max_area, area)

    # Return maximum area under
    # the given histogram
    return max_area

print(findMaxAreaHistogram(arr,n))
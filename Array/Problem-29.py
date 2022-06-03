import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')



# Trapping Rain Water 
# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output:
# 10

# Input:
# N = 4
# arr[] = {7,4,0,9}
# Output:
# 10
# Explanation:
# Water trapped by above 
# block of height 4 is 3 units and above 
# block of height 0 is 7 units. So, the 
# total unit of water trapped is 10 units.


arr=[3,0,0,2,0,4]
n=len(arr)


# def trappingOfWater(arr,n):
#     left=[-1]*n
#     right=[-1]*n


#     #Store the maximum height towards left from ith position in left array
#     left[0]=arr[0]
#     for i in range(1,n):
#         left[i]=max(left[i-1],arr[i])

#     #Store the maximum height towards right from ith position in right array
#     right[n-1]=arr[n-1]
#     for i in range(n-2,-1,-1):
#         right[i]=max(right[i+1],arr[i])

#     #Formula of water stored at ith position 
#     #water[i]=minimum(left[i],right[i])-arr[i]
#     water=0
#     for i in range(n):
#         water+=min(left[i],right[i])-arr[i]
    
#     return water 



#=========================================================================

#Solution 2 : O(n) TC and O(1) SC

def trappingOfWater(arr,n):
	left = 0
	right = n-1

	# To store Left max and right max
	# for two pointers left and right
	l_max = 0
	r_max = 0

	# To store the total amount
	# of rain water trapped
	result = 0
	while (left <= right):
		
		# We need check for minimum of left
		# and right max for each element
		if r_max <= l_max:
			
			# Add the difference between
			#current value and right max at index r
			result += max(0, r_max-arr[right])
			
			# Update right max
			r_max = max(r_max, arr[right])
			
			# Update right pointer
			right -= 1
		else:
			
			# Add the difference between
			# current value and left max at index l
			result += max(0, l_max-arr[left])
			
			# Update left max
			l_max = max(l_max, arr[left])
			
			# Update left pointer
			left += 1
	return result


print(trappingOfWater(arr, n))
    

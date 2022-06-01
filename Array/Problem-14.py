import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/input.txt', 'r')


#Merge Intervals
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

intervals = [[1,3],[2,6],[8,10],[15,18]]

def meregeIntervals(intervals):
    intervals.sort()

    n = len(intervals)
    ans = []
    ans.append(intervals[0])
    i = 1

    curIndex = 0
    while(i < n):
        cur = ans[curIndex]
        next = intervals[i]

        if(cur[-1] >= next[0]):
            temp = [min(cur[0], next[0]), max(cur[-1], next[-1])]
            ans[curIndex] = temp
            i += 1
        else:
            ans.append(next)
            curIndex += 1
            i += 1
    return ans


print(meregeIntervals(intervals))
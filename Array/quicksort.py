import sys
sys.stdout = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/output.txt', 'w')
sys.stdin = open('E:/Computer Engineering/SE COMP 2020/Data Structures/DSA-Sheet/input.txt', 'r')


array=[10, 7, 8, 9, 1, 5]

def partition(array,low,high):
    pivot=array[high]
    i=low

    for j in range(low,high):
        if(array[j]<=pivot):
            array[i],array[j]=array[j],array[i]
            i+=1
    
    array[high],array[i]=array[i],array[high]
    return i

def quickSort(array, low, high):
    if(low<high):
        pivot=partition(array,low,high)
        quickSort(array, low, pivot-1)
        quickSort(array, pivot+1, high)

print(array)

quickSort(array, 0, len(array)-1)

print(array)
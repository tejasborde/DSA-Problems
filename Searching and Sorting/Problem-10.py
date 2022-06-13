#Find pair with given difference

#Solution 1 : will be bruteforce with two loops


#Solution 2 : Using sorting the array and using two pointers

def findPair(self, arr, L,N):
    arr.sort()

    i=0
    j=1

    while(i<L-1 and j<L-1):
        diff=arr[j]-arr[i]
        if(diff==N and i!=j):
            return True
        elif(diff<N):
            j+=1
        else:
            i+=1
    return False
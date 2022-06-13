def countSquares(self, N):
    count=0
    i=1
    while(True):
        if(i**2<N):
            count+=1
        else:
            break
        i+=1
    return count
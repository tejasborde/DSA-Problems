#Find Middle with Less comparisons


def findMiddle(A,B,C):
    if((B<C and B>A) or (B<A and B>C)):
        return B
    if((C<B and C>A) or (C<A and C>B)):
        return C
    return A 

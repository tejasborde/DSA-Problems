arr1 = [1, 5, 9, 10, 15, 20 ];
arr2 = [2, 3, 8, 13 ];
 
# Function to merge two arrays
def merge(arr1,arr2,m, n):
    i = 0;
    j = 0;
    k = n - 1;
    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i+=1;
        else:
            temp = arr2[j];
            arr2[j] = arr1[k];
            arr1[k] = temp;
            j += 1;
            k -= 1;
         
    arr1.sort();
    arr2.sort();



merge(arr1,arr2,len(arr1), len(arr2))

print(arr1)
print(arr2)
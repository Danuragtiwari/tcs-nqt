#[Rotate array by K elements – Block Swap Algorithm](https://takeuforward.org/data-structure/rotate-array-by-k-elements-block-swap-algorithm/)
# Input: N = 5, array[] = {1,2,3,4,5} K=2
# Output: {3,4,5,1,2}

arr=[8,7,1,6,5,9]
k=2 
n=len(arr)
print(arr[k%n:]+arr[:k%n])
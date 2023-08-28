#[Rearrange array in increasing-decreasing order](https://takeuforward.org/data-structure/rearrange-array-in-increasing-decreasing-order/)
#Input: 8 7 1 6 5 9
#Output: 1 5 6 9 8 7

arr=[8,7,1,6,5,9]

arr.sort() 
print(arr[:len(arr)//2]+list(reversed(arr[len(arr)//2:len(arr)]))) 
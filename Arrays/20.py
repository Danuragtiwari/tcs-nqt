# [Rotation of elements of array- left and right](https://takeuforward.org/data-structure/rotate-array-by-k-elements/ "Rotation of elements of array- left and right")

# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .
n=7
k=2
arr=[1,2,3,4,5,6,7]
# right
print(arr[n-(k%n):]+arr[:n-(k%n)])
# left
# Input: 
n = 6
k=3
arr = [3,7,8,9,10,11]# , k=3 , left 
# Output: 9 10 11 3 7 8
print(arr[k%n:]+arr[:k%n])
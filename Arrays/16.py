# [Find all symmetric pairs in array](https://takeuforward.org/data-structure/find-all-symmetric-pairs-in-the-array-of-pairs/ "Find all symmetric pairs in array")

# Input: [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
# Output: [2, 1] [5, 4]
# Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.
n = 5
arr = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
dist=dict()
for i in range(n):
    first=arr[i][0]
    second=arr[i][1]
    
    if second in dist and dist[second]==first:
        print(f"({first} {second})", end=" ")
    
    else:
        dist[first] = second        
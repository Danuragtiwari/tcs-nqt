# [Finding equilibrium index of an array](https://takeuforward.org/data-structure/finding-equilibrium-index-in-an-array/ "Finding equilibrium index of an array")

# Input: nums = [2,3,-1,8,4]
# Output: 3
# Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
# The sum of the numbers after index 3 is: 4 = 4

arr=[2,3,-1,8,4]
right=sum(arr)
k=False
left=0
for i in range(len(arr)):
    right-=arr[i]
    if right==left:
    
        k=True
    
        print(i)
        break
    left+=arr[i]
if k==True:
    print()
else:
    print(-1)
# [Maximum product subarray in an array](https://takeuforward.org/data-structure/maximum-product-subarray-in-an-array/)
# Input:
nums = [1,2,3,4,5,0]
# Output:
#  120

result=0
for i in range(len(nums)):
    p=nums[i]
    for j in range(i+1,len(nums)):
           result = max(result,p)
           p *= nums[j]
      
    result= max(result,p)        
print(result)
#[Find all non-repeating elements in an array](https://takeuforward.org/data-structure/find-all-the-non-repeating-elements-in-an-array/)

# Input:
#  Nums = [1,2,-1,1,3,1]
# Output:
#  2,-1,3

Nums = [1,2,-1,1,3,1]
# n=list(set
for i in Nums:
    if Nums.count(i)==1:
        print(i,end=' ')
print('')

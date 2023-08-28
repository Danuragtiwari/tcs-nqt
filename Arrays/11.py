#[Remove duplicates from a sorted array](https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/)

# Input: arr=[1,1,1,2,2,3,3,3,3,4,4]

# Output: arr=[1,2,3,4,_,_,_,_,_,_,_]

arr=[1,1,1,2,2,3,3,3,3,4,4]
l=[]
for i in range(arr):
    if i not in l:
        l.append(i)
print(l)
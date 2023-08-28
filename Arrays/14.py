#[Find all repeating elements in an array](https://takeuforward.org/data-structure/find-all-repeating-elements-in-an-array/)
# Input: 
# Arr[] = [1,1,2,3,4,4,5,2]
# Output:
#  1,2,4

arr=[1,1,2,3,4,4,5,2]
ar=list(set(arr))

a=[]
for i in ar:
    if arr.count(i)>1:
        a.append(i)
print(a)
    


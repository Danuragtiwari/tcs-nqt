#[Remove duplicates from unsorted array](https://takeuforward.org/data-structure/remove-duplicates-from-an-unsorted-array/ "Remove duplicates from unsorted array")



# Input: arr[]={2,3,1,9,3,1,3,9}
# Output:  {2,3,1,9}



arr=[2,3,1,9,3,1,3,9]
l=[]
for i in range(arr):
    if i not in l:
        l.append(i)
print(l)
#[Insertion Sort Algorithm] https://takeuforward.org/data-structure/insertion-sort-algorithm/


# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: 
# After sorting the array is: 9,13,20,24,46,52

arr=[13,46,24,52,20,9]
for i in range(1,len(arr)):
    j=i-1
    key=arr[i]
    while j >= 0 and key< arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)
        
    
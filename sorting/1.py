# [Bubble Sort]  https://takeuforward.org/data-structure/bubble-sort-algorithm/




arr=[13, 46, 24, 52, 20, 9]
n=len(arr)

for i in range(n):
    swapped=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True  
    if not swapped:
        print(True,arr)
        break
print(arr)
            

























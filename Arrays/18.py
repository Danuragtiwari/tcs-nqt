# [Replace each element of the array by its rank in the array](https://takeuforward.org/data-structure/replace-elements-by-its-rank-in-the-array/ "Replace each element of the array by its rank in the array")



n = 6
arr = [20, 15, 26, 2, 98, 6]

for i in range(n):
    s = set()
    for j in range(n):
        if arr[j] < arr[i]:
            s.add(arr[j])
    print(len(s) + 1, end=" ")
    
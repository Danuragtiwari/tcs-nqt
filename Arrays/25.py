# [Check if Array is a subset of another array or not](https://takeuforward.org/data-structure/check-if-array-is-subset-of-another-array/ "Check if Array is a subset of another array or not")

arr1 = [1, 2, 3]
arr2 = [3, 2, 1, 4, 5]
def is_subset(arr1, arr2):
    return all(element in arr2 for element in arr1)
print(is_subset(list(set(arr1)),list(set(arr2))))
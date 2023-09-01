#[Selection Sort]  https://takeuforward.org/sorting/selection-sort-algorithm/



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("Sorted array:", arr)
# In this code:

# arr is the input list to be sorted.
# The outer loop iterates through each element in the list.
# The inner loop finds the minimum element in the unsorted part of the list by comparing each element with the current minimum. The index of the minimum element is stored in min_index.
# After finding the minimum element, it is swapped with the element at the current position in the outer loop.
# This process is repeated until the entire list is sorted.
# When you run this code with the example input list, it will correctly sort the list using the selection sort algorithm.




# Was this response better or worse?
# Better
# Worse
# Same



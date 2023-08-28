# [Sorting elements of an array by frequency](https://takeuforward.org/data-structure/sort-elements-of-an-array-by-frequency/ "Sorting elements of an array by frequency")


# Input: N = 8, array[] = {1,2,3,2,4,3,1,2}
# Output: 2 2 2 1 1 3 3 4 

arr = [1, 2, 3, 2, 4, 3, 1, 2]
dict1 = dict()
for i in arr:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

def custom_sort(item):
    return item[1]


sorted_dict1 = dict(sorted(dict1.items(), key=custom_sort, reverse=True))

# Create a list of elements sorted by frequency
sorted_elements = []

for key, value in sorted_dict1.items():
    sorted_elements.extend([key] * value)

print(sorted_elements)
#[Second Smallest and Second Largest element in an array](https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/)
   
arr=[1,2,-1,-1,-5,-9,9,320]
arr=list(set(arr))
arr.remove(min(arr)) 
arr.remove(max(arr))

print(min(arr),max(arr))  
   
#arr = [1, 2, -1, -1, -5, -9, 9, 9]
# sorted_arr = sorted(arr)
# second_smallest = sorted_arr[1]  # Index 1 is the second smallest element
# second_largest = sorted_arr[-2]  # Index -2 is the second largest element
# print(second_smallest, second_largest)   
   
   
   
   
   
   
   
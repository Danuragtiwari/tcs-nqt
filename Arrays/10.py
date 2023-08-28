#[Find the median of the given array](https://takeuforward.org/data-structure/find-median-of-the-given-array/)

arr=[1,2,3,4943,49]
n=len(arr)
if n%2==0:
    print((arr[(n)/2]+arr[n//2 -1])/2)
else:
    print(arr[n//2])
    
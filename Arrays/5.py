#[Count frequency of each element in an array](https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/)

a=[10,5,10,15,10,5]
arr=list(set(a)) 

for i in arr:
    print(i,a.count(i))
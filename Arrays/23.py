# Sort an array according to the order defined by another array #https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/

# Input: A1[] = {2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8}
#            A2[] = {2, 1, 8, 3}
# Output: A1[] = {2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9}


# Input: A1[] = {4, 5, 1, 1, 3, 2}
#            A2[] = {3, 1}

# a1=[2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a1=[4, 5, 1, 1, 3, 2]
temp=[]
# a2=[2,1,8,3]
a2=[3, 1]

for i in a2:
    while i in a1:
        temp.append(i)
        a1.remove(i)
print(temp+sorted(a1))












# [Adding Element in an array](https://takeuforward.org/data-structure/adding-element-in-an-array/)



# Input: N = 5, array[] = {1,2,3,4,5}
# insertbeginning(6)
# insertending(7)
# insertatpos(8,4)
# C

arr=[1,2,3,4,5]
def insertbeginning(i):
    arr.insert(0,i)
def insertending(i):
    arr.append(i)
def insertatpos(p,i):
    arr.insert(i,p)

insertbeginning(6)
insertending(7)
insertatpos(8,4)
print(arr)
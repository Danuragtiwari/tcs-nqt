# https://takeuforward.org/data-structure/print-all-the-duplicates-in-the-string/

# Input:
#  str= "sinstriiintng"
# Output:
# i - 4
# n - 3
# s - 2
# t - 2
s='sinstriiintng'
dict1={}
for i in s:
    if i not in dict1:
        dict1[i]=1 
    else:
        dict1[i]+=1 
# print(dict1)
ans=[char+'-'+str(value) for char,value in dict1.items() if value>1]
ans.sort()
print(ans)
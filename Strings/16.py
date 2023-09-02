# https://takeuforward.org/data-structure/maximum-occurring-character-in-a-string/

# Input: str = “takeuforward”
# Output: a
# Explanation: The character 'a' and 'r’ have the same  maximum occurrence i.e 2. Hence we can print any one of them
# maxc=0
dict1={}
s='takeuforward'
for i in s:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1 

maxvalue=max(dict1.values())
ans=[char for char,value in dict1.items() if value==maxvalue]
print(ans[0])

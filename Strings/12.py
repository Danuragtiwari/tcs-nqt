#https://takeuforward.org/data-structure/find-non-repeating-characters-of-a-string/

# Input: string = “google”
# Output: l,e

# Explanation: Non repeating characters are l,e.
ans=[]
s='google'
for i in s:
    if s.count(i)==1:
        ans.append(i)
print(*ans)
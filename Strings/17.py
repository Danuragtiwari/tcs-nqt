# https://takeuforward.org/data-structure/remove-all-duplicates-from-a-string/

# Example 1:
# Input: s = "bcabc"
# Output: “bca"

s = "bcabc"
ns=''
for i in s:
    if i not in ns:
        ns+=i  
print(ns)
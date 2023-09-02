# https://takeuforward.org/data-structure/write-a-program-to-sort-characters-in-a-string/


# Example 1:
# Input: String str = “zxcbg”
# Output: bcgxz
# Explanation: After sorting we get string as bcgxz

s='zxcbg'
l=list(s)
l.sort()
s=''.join(l)
print(l,s)
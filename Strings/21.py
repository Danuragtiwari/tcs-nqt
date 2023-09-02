# https://takeuforward.org/data-structure/find-the-largest-word-in-a-string/

# Input: string s=”Google Doc”
# Output: “Google”

# Explanation: Google is the largest word in the given string.

s='Google Doc  hduihhhhhhhhhh  z'
ls=s.split(' ')
print(max(ls,key=len))
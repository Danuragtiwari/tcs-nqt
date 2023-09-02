#https://takeuforward.org/data-structure/remove-characters-from-first-string-present-in-the-second-string/


# Input: String str1 = “abcdef”
#        String str2 = “cefz”
# Output: abd
# Explanation: The common characters in both strings are c, e, f.
# So after removing these characters from string 1 we get string resulting string as abd.


str1='abcdef'
str2='cefz'

ans=''
for i in str1:
    if i in str2:
        ans+=i 
print(ans)
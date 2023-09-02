# https://takeuforward.org/string/capitalize-first-and-last-character-of-each-word-of-a-string/




# Example 1:
# Input: String str = "take u forward is awesome"
# Output: “TakE U ForwarD IS AwesomE”
# Explanation: We get the result after capitalizing the first and last character of each word of a string

s='take u forward is awesome'
s=s.split(' ')
ans=''
for i in s:
    if len(i)>=2:
        ans+=i[0].upper()+i[1:-1]+i[-1].upper()+' '
    elif len(i)==1:
        ans+=i.upper()+' '
    else:
        # continue  
        ans+=''
# ans=' '
print(ans.strip())
        
    
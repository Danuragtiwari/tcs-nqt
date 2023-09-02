# https://takeuforward.org/data-structure/remove-all-vowels-from-the-string/



# Input: Str = “take u forward”
# Output: tk  frwrd
# Explanation: All vowels are removed from the given String.

s='take u forward'
news=''
for i in s:
    if i not in ['A','E','O','I','U','a','e','i','o','u']:
        news+=i
print(news)
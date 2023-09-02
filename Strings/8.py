# https://takeuforward.org/data-structure/remove-brackets-from-an-algebraic-expression/

# Input: “a+((b-c)+d)”
# Output: “a+b-c+d”
# Explanation: Removed all the brackets in the algebric expression.

s='a+((b-c)+d)'
news=''

for i in s:
    if i not in ['(',')']:
        news+=i
print(news)
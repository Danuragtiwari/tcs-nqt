# https://takeuforward.org/data-structure/remove-characters-from-a-string-except-alphabets/

# Input: string str = "take12% *&u ^$#forward"
# Output: takeuforward  


s1='take12% +&u ^$#forward'
news=''
for i in s1:
    if i not in ['%',' ','&','#','^','$','+','-','1','2','3','4','5','6','7','8','9','0','@','*']:
        news+=i
print(news)


#https://takeuforward.org/data-structure/count-number-of-vowels-consonants-spaces-in-string/

# Input: string str=”Take u forward is Awesome”
# Output: 
# Vowels: 10
# Consonants: 11
# White spaces: 4
# Explanation:  

string='Take u forward is Awesome'
vow=0 
cons=0
whspc=0
for i in string:
    if i==' ':
        whspc+=1 
    elif i in ['A','E','I','O','U','a','e','i','o','u']:
        vow+=1
    else:
        cons+=1 
print(cons,vow,whspc)
        

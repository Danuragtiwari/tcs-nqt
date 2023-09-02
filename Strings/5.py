# https://takeuforward.org/data-structure/remove-spaces-from-a-string/

# Input: str = “Take you forward” 
# Output: Takeyouforward

s='Take you forward'
news=''
for i in s:
    if i==' ':
        continue  
    news+=i
print(news)
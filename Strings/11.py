#https://takeuforward.org/data-structure/calculate-frequency-of-characters-in-a-string/



# Input: takeuforward
# Output: a2 d1 e1 f1 k1 o1 r2 t1 u1 w1 
# Explanation: Count of every character of string is printed.

d={}
s='takeuforward'
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
# print(d)
for key,value in d.items():
    print(key+str(value))
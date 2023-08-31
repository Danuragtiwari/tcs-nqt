# Prime numbers in a given range # https://takeuforward.org/data-structure/prime-numbers-in-a-given-range/



# Examples:
# Input: 2 10
# Output: 2 3 5 7 
# Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.
def check(i):
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c+=1
    if c==1:
        return True 
    return False
s=2 
e=10
for i in range(s,e+1):
    if check(i):
        print(i)







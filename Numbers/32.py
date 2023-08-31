# https://takeuforward.org/data-structure/replace-all-the-0s-with-1-in-a-given-integer/


# Input: N = 102003
# Output: 112113
# Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.


n=102003 
n=str(n)
n.replace('0','1')
print(str(n))
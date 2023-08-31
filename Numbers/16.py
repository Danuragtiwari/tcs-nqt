# https://takeuforward.org/data-structure/maximum-and-minimum-digit-in-a-number/


# Example 1:
# Input: N = 2746
# Output: Largest digit: 7
#         Smallest digit: 2
n=2746 
maxi=int(str(n)[0])
mini=float('inf')
for i in str(n):
    maxi=max(maxi,int(i))
    mini=min(mini,int(i))
print(maxi,mini)
    
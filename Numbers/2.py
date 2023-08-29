#[Find all Palindrome numbers in a given range](https://takeuforward.org/data-structure/find-all-palindrome-numbers-in-a-given-range/)

# Example 1:
# Input: min = 10 , max = 50
# Output: 11 22 33 44 
# Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.


min1=10 
max1=50 
for i in range(min1,max1+1):
    if str(i)==str(i)[::-1]:
        print(i)
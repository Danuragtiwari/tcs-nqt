# [Leap Year or not](https://takeuforward.org/data-structure/check-if-given-year-is-a-leap-year-or-not/ "https://takeuforward.org/data-structure/check-if-given-year-is-a-leap-year-or-not/")

# Input: 1996
# Output: Yes
# Explanation: Since 1996 is a leap year answer is “Yes”.
y=1999
if (y%4==0 and y%100!=0) or (y%400==0):
    print(True)

else:
    print(False)
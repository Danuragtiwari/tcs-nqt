# https://takeuforward.org/interviews/tcs-nqt-coding-sheet-tcs-coding-questions/


# Eample 1:.
# Input: N = 1100110
# Output: 146
# Explaxnation: 1100110 when converted to octal number is “146”.



s = "1100110"
n = len(s)

# Ensure the length of s is a multiple of 3 by adding leading zeros if necessary
if n % 3 == 1:
    s = "00" + s
elif n % 3 == 2:
    s = "0" + s

n = len(s)
ans = ""

for i in range(0, n, 3):
    temp = (int(s[i]) - 0) * 4 + (int(s[i + 1]) - 0) * 2 + (int(s[i + 2]) - 0) * 1
    print(temp)
    ans += str(temp)

print(ans)




























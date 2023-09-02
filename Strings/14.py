# https://www.geeksforgeeks.org/count-common-subsequence-in-two-strings/

# Input : S = “ajblqcpdz”, T = “aefcnbtdi” 
# Output : 11 
# Common subsequences are : { “a”, “b”, “c”, “d”, “ab”, “bd”, “ad”, “ac”, “cd”, “abd”, “acd” }
a='string'
b='sting'
# Geeting tle
# n=len(a)
# m=len(b)
# dp=[[0]*(m+1) for i in range(n+1)]
# for i in range(1,n+1):
# 		for j in range(1,m+1):
# 		    if a[i-1]==b[j-1]:
# 		        dp[i][j]=1 + dp[i][j - 1] +dp[i - 1][j]
                                
# 		    else:
# 		        dp[i][j]=dp[i][j - 1] + dp[i - 1][j] -dp[i - 1][j - 1]
                            
# return dp[n][m]


# using set
c = set(a) & set(b)
print(c)

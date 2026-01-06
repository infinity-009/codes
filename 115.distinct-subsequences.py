# #
# # @lc app=leetcode id=115 lang=python
# #
# # [115] Distinct Subsequences
# #
# # https://leetcode.com/problems/distinct-subsequences/description/
# #
# # algorithms
# # Hard (51.12%)
# # Likes:    7296
# # Dislikes: 319
# # Total Accepted:    643.4K
# # Total Submissions: 1.3M
# # Testcase Example:  '"rabbbit"\n"rabbit"'
# #
# # Given two strings s and t, return the number of distinct subsequences of s
# # which equals t.
# # 
# # The test cases are generated so that the answer fits on a 32-bit signed
# # integer.
# # 
# # 
# # Example 1:
# # 
# # 
# # Input: s = "rabbbit", t = "rabbit"
# # Output: 3
# # Explanation:
# # As shown below, there are 3 ways you can generate "rabbit" from s.
# # rabbbit
# # rabbbit
# # rabbbit
# # 
# # 
# # Example 2:
# # 
# # 
# # Input: s = "babgbag", t = "bag"
# # Output: 5
# # Explanation:
# # As shown below, there are 5 ways you can generate "bag" from s.
# # babgbag
# # babgbag
# # babgbag
# # babgbag
# # babgbag
# # 
# # 
# # Constraints:
# # 
# # 
# # 1 <= s.length, t.length <= 1000
# # s and t consist of English letters.
# # 
# # 
# #

# # @lc code=start
# class Solution(object):
    
#     def numDistinct(self, s, t):
        
#         from functools import lru_cache
        
#         """
#         :type s: str
#         :type t: str
#         :rtype: int
#         """
        
#         n=len(s)
        
#         m=len(t)
        
#         ans=[0]
        
        
#         dp=[[-1]*n for _ in range(m)]
        
        
#         def get_combinations(n,m):
            
#             print(n,m,"ans",ans[0])
            
#             if m<0:
#                 ans[0]+=1
#                 return 
            
#             if n<0: return
                
#             for i in range(n,-1,-1):
#                 if s[i]==t[m]:
#                     print(i,m)
#                     get_combinations(i-1,m-1)
                     
#         get_combinations(n-1,m-1)
        
#         return ans[0]
                    
            
# test=Solution()

# print("ans",test.numDistinct("rabbbitt","rabit"))
# # @lc code=end


# """

# # Input: s = "babgbag", t = "bag"

# """



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[i][0]=1
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j]+=dp[i-1][j]
                
                if s[i-1]==t[j-1]:
                    dp[i][j]+=dp[i-1][j-1]    
   
                    
        return dp[n][m]





from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @lru_cache(None)
        def dfs(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            
            return dfs(i-1,j) + (dfs(i-1,j-1) if s[i]==t[j] else 0)

        return dfs(len(s)-1,len(t)-1)
            
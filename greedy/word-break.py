class Solution:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #dp[i]: s[0:i)是不是一个wordBreak
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] is True and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

sl = Solution()

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]


print(sl.wordBreak(s, wordDict))


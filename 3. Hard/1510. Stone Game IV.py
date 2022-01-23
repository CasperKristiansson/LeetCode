class Solution:
    def winnerSquareGame(self, n: int) -> bool:       
        i = 1
        while True:
            print(n ** 0.5)
            if n ** 0.5 % 1 == 0:
                print(n)
                return i == 1

            n -= 1
            i = -i
            if n == 0:
                return i == 1
    
    def winnerSquareGame2(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if dp[i-k*k] == False:
                    dp[i] = True
                    break
        return dp[n]


print(Solution().winnerSquareGame2(15))
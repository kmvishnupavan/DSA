class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
            
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
       
        dp = [[0] * n for _ in range(n)]
        
        max_l = [[0] * n for _ in range(n)]
        
        max_r = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                target = pref[j + 1] - pref[i]  
                
                
                low, high = i, j - 1
                m = i - 1
                
                while low <= high:
                    mid = (low + high) // 2
                    if (pref[mid + 1] - pref[i]) * 2 <= target:
                        m = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                        
                ans = 0
                if m >= i:
                    ans = max_l[i][m]
                    
                    
                    if (pref[m + 1] - pref[i]) * 2 == target:
                        ans = max(ans, max_r[m + 1][j])
                    else:
                        if m + 2 <= j:
                            ans = max(ans, max_r[m + 2][j])
                else:
                    
                    ans = max_r[i + 1][j]
                    
                dp[i][j] = ans
                
                max_l[i][j] = max(max_l[i][j - 1], target + ans)
                max_r[i][j] = max(max_r[i + 1][j], target + ans)
                
        return dp[0][n - 1]
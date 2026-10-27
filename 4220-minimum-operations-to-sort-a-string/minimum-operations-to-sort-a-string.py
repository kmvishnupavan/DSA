class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        
        # Check if already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
            
        # If length is 2 and not sorted, it's impossible
        if n == 2:
            return -1
            
        min_idx = 0
        max_idx = 0
        for i in range(n):
            if s[i] < s[min_idx]:
                min_idx = i
            if s[i] >= s[max_idx]:
                max_idx = i
                
        # Smallest element starts at index 0 or largest element ends at index n-1
        if min_idx == 0 or max_idx == n - 1:
            return 1
            
        # Smallest element is at the very end and largest is at the very beginning
        if min_idx == n - 1 and max_idx == 0:
            return 3
            
        # All other cases take 2 operations
        return 2
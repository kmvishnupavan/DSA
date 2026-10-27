class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            doubled = a + a
            m = len(b)

            lps = [0] * m
            j = 0
            i = 1

            while i < m:
                if b[i] == b[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                elif j:
                    j = lps[j - 1]
                else:
                    i += 1

            i = 0
            j = 0

            while i < len(doubled) - 1:
                if doubled[i] == b[j]:
                    i += 1
                    j += 1
                    if j == m:
                        return True
                elif j:
                    j = lps[j - 1]
                else:
                    i += 1

            return False

        for k in range(1, n + 1):
            if n % k:
                continue

            possible = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                target_block = target[start:start + k]

                if not is_rotation(block, target_block):
                    possible = False
                    break

            if possible:
                ans += k

        return ans
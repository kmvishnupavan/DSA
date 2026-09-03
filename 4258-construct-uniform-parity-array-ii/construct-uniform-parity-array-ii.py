class Solution:
    def uniformArray(self, nums1):
        mn = min(nums1)
        target = mn % 2

        min_odd = float('inf')

        for x in nums1:
            if x % 2 == 1:
                min_odd = min(min_odd, x)

        for x in nums1:
            if x % 2 == target:
                continue

            # x needs to become target parity.
            # This requires subtracting an odd number.
            # That odd number must be smaller than x.
            if min_odd >= x:
                return False

        return True
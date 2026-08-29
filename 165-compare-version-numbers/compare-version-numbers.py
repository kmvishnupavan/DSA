class Solution:
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        n = max(len(v1), len(v2))

        for i in range(n):
            if i < len(v1):
                num1 = int(v1[i])
            else:
                num1 = 0

            if i < len(v2):
                num2 = int(v2[i])
            else:
                num2 = 0

            if num1 < num2:
                return -1

            if num1 > num2:
                return 1

        return 0
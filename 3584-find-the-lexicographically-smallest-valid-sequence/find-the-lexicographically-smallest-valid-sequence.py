class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[j] = earliest index where word2[j:]
        # can be matched exactly.
        # -1 means it is impossible.
        suf = [-1] * (m + 1)

        suf[m] = n

        p = n - 1

        for j in range(m - 1, -1, -1):
            while p >= 0 and word1[p] != word2[j]:
                p -= 1

            if p < 0:
                break

            suf[j] = p
            p -= 1

        ans = []
        i = 0
        j = 0
        changed = False

        while i < n and j < m:

            # Characters match, so take this index.
            if word1[i] == word2[j]:
                ans.append(i)
                i += 1
                j += 1

            # Characters don't match.
            elif not changed:
                # Use this index for the one allowed change.
                #
                # The remaining suffix must be matched exactly.
                if j + 1 == m or (
                    suf[j + 1] != -1 and suf[j + 1] > i
                ):
                    ans.append(i)
                    i += 1
                    j += 1
                    changed = True
                else:
                    i += 1

            else:
                i += 1

        if j == m:
            return ans

        return []
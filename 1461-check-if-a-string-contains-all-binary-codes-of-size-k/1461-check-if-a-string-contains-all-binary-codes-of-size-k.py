class Solution(object):
    def hasAllCodes(self, s, k):
        left = 0
        seen = set()

        for right in range(len(s)):

            if right - left + 1 == k:
                substring = s[left:right + 1]
                seen.add(substring)

                left += 1

        return len(seen) == 2 ** k
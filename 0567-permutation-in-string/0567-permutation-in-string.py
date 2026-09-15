class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        left = 0

        for right in range(len(s2)):
            char = s2[right]

            window[char] = window.get(char, 0) + 1

            if right - left + 1 == len(s1):

                if window == need:
                    return True

                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

        return False

  

      
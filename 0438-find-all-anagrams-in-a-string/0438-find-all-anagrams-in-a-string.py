class Solution(object):
    def findAnagrams(self, s, p):
        answer = []
        left = 0

        p_freq = {}

        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

        window_freq = {}

        for right in range(len(s)):
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            if right - left + 1 == len(p):

                if window_freq == p_freq:
                    answer.append(left)

                window_freq[s[left]] -= 1

                if window_freq[s[left]] == 0:
                    del window_freq[s[left]]

                left += 1

        return answer
        
        

       
        
class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        freq = {}
        max_freq = 0 
        answer = 0

        for right in range(len(s)):

            char = s[right]

            freq[char]= freq.get(char,0) + 1 

            max_freq = max(max_freq , freq[char]) 

            while (right -  left + 1) - max_freq > k :

                   freq[s[left]] -= 1

                   left += 1 

            answer = max(answer , right - left + 1)

        return answer 



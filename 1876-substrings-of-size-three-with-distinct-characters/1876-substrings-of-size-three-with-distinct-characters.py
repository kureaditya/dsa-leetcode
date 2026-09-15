class Solution(object):
    def countGoodSubstrings(self, s):
        count=0
        left=0
        freq={}
        for right in range(len(s)) :

            freq[s[right]] = freq.get(s[right], 0) + 1

            if right - left + 1 == 3 :

                if len(freq) == 3 :
                  count += 1

                freq[s[left]] -= 1 

                if freq[s[left]] == 0 :
                    del  freq[s[left]]

                left += 1

        return count




       
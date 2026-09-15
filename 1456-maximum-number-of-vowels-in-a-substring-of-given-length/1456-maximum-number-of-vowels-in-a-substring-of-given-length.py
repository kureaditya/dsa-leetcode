class Solution(object):
    def maxVowels(self, s, k):
        vowels="aeiou"
        left=0
        count=0
        max_count=0

        for right in range(len(s)) :
            if s[right] in vowels :
                count=count+1

            if right-left+1 == k :
                max_count = max(max_count, count)
            
                if s[left] in vowels:
                   count=count-1
             
                left=left+1
        return max_count
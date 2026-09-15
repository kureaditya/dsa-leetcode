class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        left = 0
        total_cost = 0
        answer = 0

        for right in range(len(s)):
            total_cost += abs(ord(s[right]) - ord (t[right])) 

            while total_cost > maxCost :
                total_cost -= abs(ord(s[left]) - ord (t[left])) 
                left += 1 

            answer = max( answer , right - left + 1 )
        
        return answer 






        
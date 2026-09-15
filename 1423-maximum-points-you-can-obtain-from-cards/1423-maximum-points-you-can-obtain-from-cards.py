class Solution(object):
    def maxScore(self, cardPoints, k):
        total_sum = sum(cardPoints)
        window_size = len(cardPoints)-k
        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum

        left = 0

        for right in range(window_size, len(cardPoints)) :

             window_sum = window_sum - cardPoints[left] + cardPoints[right]
             min_window_sum = min(min_window_sum , window_sum)

             left+=1
        return total_sum - min_window_sum 
        
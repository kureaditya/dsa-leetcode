class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        answer = 0

        for right in range(len(nums)) :
            
            if nums[right] == 0 :
                zeros += 1 
            
            while zeros > 1 :

                if nums[left] == 0 :

                    zeros -= 1

                left += 1

            answer = max(answer , right - left )

        return answer
 



             


       
class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        answer = float("inf")
        left = 0

        for right in range(k-1 , len(nums)) :

            diff = nums[right] - nums[left] 

            answer = min(answer,diff)

            left += 1
        
        return answer
    
    
 
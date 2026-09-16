class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0:
            return -1

        left = 0
        window_sum = 0
        answer = -1

        for right in range(len(nums)):
            window_sum += nums[right]

            while left <= right and window_sum > target:
                window_sum -= nums[left]
                left += 1

            if window_sum == target:
                answer = max(answer, right - left + 1)

        if answer == -1:
            return -1

        return len(nums) - answer
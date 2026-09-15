class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        window_sum = 0
        freq = {}
        answer = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 == k:

                if len(freq) == k:
                    answer = max(answer, window_sum)

                window_sum -= nums[left]

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

        return answer



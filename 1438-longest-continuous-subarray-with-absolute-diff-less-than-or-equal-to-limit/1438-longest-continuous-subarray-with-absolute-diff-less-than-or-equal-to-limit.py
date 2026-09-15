class Solution(object):
    def longestSubarray(self, nums, limit):
        from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        left = 0
        answer = 0

        max_dq = deque()
        min_dq = deque()

        for right in range(len(nums)):

            while max_dq and max_dq[-1] < nums[right]:
                max_dq.pop()

            while min_dq and min_dq[-1] > nums[right]:
                min_dq.pop()

            max_dq.append(nums[right])
            min_dq.append(nums[right])

            while max_dq[0] - min_dq[0] > limit:

                if max_dq[0] == nums[left]:
                    max_dq.popleft()

                if min_dq[0] == nums[left]:
                    min_dq.popleft()

                left += 1

            answer = max(answer, right - left + 1)

        return answer
        
        
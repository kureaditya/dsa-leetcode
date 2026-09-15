class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        avgs = [-1]*n

        window_size = 2*k+1
        if window_size > n :
         return avgs

        window_sum = sum(nums[:window_size])

        avgs[k] = window_sum //window_size

        left = 0

        for right in range(window_size,n):
            
            window_sum -= nums[left]
            window_sum += nums[right]

            left += 1

            avgs[left + k] = window_sum // window_size

        return avgs
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count=0
        window_sum=0
        left=0

        for right in range (len(arr)) :
            window_sum += arr[right] 

            if right - left + 1 == k :

                if window_sum >= k * threshold :
                     count += 1
                     
                window_sum -= arr[left]
                left += 1

        return count


                

        
        
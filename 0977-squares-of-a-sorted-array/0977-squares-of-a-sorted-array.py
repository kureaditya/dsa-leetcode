class Solution(object):
    def sortedSquares(self, nums):

        left=0
        right=len(nums)-1

        result=[0]*len(nums)

        position=len(nums)-1

        
        while left <= right :

            if abs(nums[left]) > abs(nums[right]):

                result[position]=nums[left]*nums[left]

                left=left+1

            
            else:

                result[position]=nums[right]*nums[right]

                right=right-1

            position = position-1
        return result



                



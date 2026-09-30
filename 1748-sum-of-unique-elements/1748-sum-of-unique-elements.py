class Solution(object):
    def sumOfUnique(self, nums):
        freq={}
        answer = 0

        for num in nums :
            freq[num]=freq.get(num,0)+1

        for num in freq :
            if freq[num] == 1 :
                answer += num
        
        return answer





        
        
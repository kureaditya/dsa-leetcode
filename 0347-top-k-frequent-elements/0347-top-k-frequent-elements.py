class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []

        for item in sorted_freq[:k]:
            result.append(item[0])

        return result

        




            



       






        
       
        
class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        result = set()

        for x in nums2:
            if x in set1:
                result.add(x)

        return list(result)
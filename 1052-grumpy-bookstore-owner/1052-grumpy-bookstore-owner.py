class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        base = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        left = 0
        window = 0
        max_extra = 0

        for right in range(len(customers)):

            if grumpy[right] == 1:
                window += customers[right]

            if right - left + 1 == minutes:

                max_extra = max(max_extra, window)

                if grumpy[left] == 1:
                    window -= customers[left]

                left += 1

        return base + max_extra
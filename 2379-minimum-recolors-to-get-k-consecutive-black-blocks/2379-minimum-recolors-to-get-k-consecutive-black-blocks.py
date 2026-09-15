class Solution(object):
    def minimumRecolors(self, blocks, k):
        left = 0
        window_w = 0
        answer = float("inf")

        for right in range(len(blocks)):

            if blocks[right] == "W":
                window_w += 1

            if right - left + 1 == k:

                answer = min(window_w, answer)

                if blocks[left] == "W":
                    window_w -= 1

                left += 1

        return answer



        
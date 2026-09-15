class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        answer = [0] * n

        if k == 0:
            return answer

        for i in range(n):
            window_sum = 0

            if k > 0:
                for j in range(1, k + 1):
                    window_sum += code[(i + j) % n]

            else:
                for j in range(1, abs(k) + 1):
                    window_sum += code[(i - j) % n]

            answer[i] = window_sum

        return answer
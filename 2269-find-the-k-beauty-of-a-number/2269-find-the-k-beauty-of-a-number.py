class Solution(object):
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0

        for i in range(len(s)-k+1):
            window=int(s[i:i+k])

            if window != 0 and num % window == 0 :

                count += 1
        
        return count 


        
       


       
class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        freq = {}
        answer = 0

        for right in range(len(fruits)) :
            fruit = fruits[right]

            freq[fruit] = freq.get(fruit,0) + 1

            while len(freq) > 2 :
                left_fruit = fruits[left]
                freq[left_fruit] -= 1

                if freq[left_fruit] == 0 :
                    del freq[left_fruit] 
                
                left += 1

            answer = max(answer , right - left + 1) 

        return answer

class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        vowels="aeiouAEIOU"
        left=0
        right=len(s)-1

        while left < right :

            if s[left] not in vowels :
                left = left+1 

            elif s[right] not in vowels :
                right = right -1 

            else: 
                s[left],s[right]=s[right],s[left]

                left = left+1 
                right = right-1
        return "".join(s)
       
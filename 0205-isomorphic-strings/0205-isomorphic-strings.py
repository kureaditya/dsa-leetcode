class Solution(object):
    def isIsomorphic(self, s, t):
        map_1 = {}
        map_2 = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in map_1 and map_1[a] != b:
                return False

            if b in map_2 and map_2[b] != a:
                return False

            map_1[a] = b
            map_2[b] = a

        return True


    
    
       
       
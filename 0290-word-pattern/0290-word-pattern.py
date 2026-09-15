class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_map = {}
        word_map = {}

        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]

            if p in pattern_map and pattern_map[p] != w:
                return False

            if w in word_map and word_map[w] != p:
                return False

            pattern_map[p] = w
            word_map[w] = p

        return True

   
            
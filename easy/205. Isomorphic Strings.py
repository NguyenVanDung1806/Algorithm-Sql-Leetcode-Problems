# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.
defclass Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_map = {} #tao 1 dict luu cac gia tri
        t_map ={}
        for i in range len(s):
            s_ch = s[i]
            t_ch = t[i]
            if s_ch not in s_map :
                s_map[s_ch] = t_ch
            if t_ch not in t_map :
                t_map[t_ch] = s_ch
            if t_map[t_ch] != s_ch or s_map[s_ch] != t_ch:
                return False
        return True
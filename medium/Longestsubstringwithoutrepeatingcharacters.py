# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        map = {} # tao mot bien dictionary de chua ki tu hien tai dang empty
        max_legth = start = 0 #  tao hai bien voi bat dau  = 0 
        for i in range(0 , len(s)): # duyet mot vong for i bat dau tu 0 trong khoang len cua chuoi minh da cho
            if s[i] in map and start <= map[s[i]]: # neu S[i] nam trong map 
                                                # tuc la no da xuat hien trong bien map 
                                                # gia tri max <= gia tri max tai vi tri s[i]
                start = map[s[i]] + 1           # cap nhat lai bien map tai vi tri thu i + 1 de bo qua va tiep tuc duyet phan tu tiep theo
            else: 
                max_legth = max(max_legth, i - start + 1) # neu xuat hien thi cu them vao trong map va tang them 1 de tiep tuc duyet
            map[s[i]] = i # max[i] = i 
        return (max_legth) # tra ve so ki tu khong bi duplicate trong map
    
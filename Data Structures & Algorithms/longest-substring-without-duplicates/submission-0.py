class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_len = 0
        currstr = ""
        for idx, char in enumerate(s):
            if char not in currstr:
                currstr += char
                max_len = max(len(currstr), max_len)
            else:
                start += currstr.index(char)+1
                currstr = s[start:idx+1]
        return max_len
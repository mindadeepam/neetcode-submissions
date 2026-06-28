class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_len = 0
        last_seen = {}
        for idx, char in enumerate(s):
            if char not in last_seen:
                last_seen[char] = idx
                curr_len = idx-start+1
                max_len = max(curr_len, max_len)
            else:
                start += last_seen[char]+1
                last_seen[char] = idx
        return max_len


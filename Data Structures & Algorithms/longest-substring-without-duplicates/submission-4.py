class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_len = 0
        # currstr = ""
        last_seen = {}
        curr_len=0
        for idx, char in enumerate(s):
            if (char not in last_seen) or (last_seen[char]<start):
                last_seen[char] = idx
                curr_len += 1
            elif last_seen[char]>=start:
                max_len = max((idx-start), max_len)
                start = last_seen[char]+1
                last_seen[char] = idx
                curr_len = idx-start+1

            max_len = max(curr_len, max_len)

        return max_len

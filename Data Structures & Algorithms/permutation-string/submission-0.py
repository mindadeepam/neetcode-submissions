from collections import defaultdict
class Solution:
    def get_freq_arr(self, s):
        arr = [0 for i in range(26)]
        for char in s:
            arr[ord(char)-ord("a")]+=1

        return arr

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for char in s1:
            s1_dict[char] += 1
        s1_arr = self.get_freq_arr(s1)
        
        for idx, char in enumerate(s2):
            if char not in s1_dict:
                continue
            elif char in s1_dict:
                s2_substring = s2[idx: idx+len(s1)]
                if s1_arr == self.get_freq_arr(s2_substring):
                    return True 

        return False

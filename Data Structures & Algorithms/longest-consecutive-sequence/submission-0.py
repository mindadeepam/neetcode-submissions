class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        curr_consecutive_count = 1
        max_consec_count = 1
        n = len(nums)
        for e in range(1, n):
            # print(f"e {e}, nums[e]: {nums[e]}, curr_consec: {curr_consecutive_count}")
            if nums[e]-nums[e-1]==1:
                curr_consecutive_count += 1
            if nums[e]-nums[e-1]>1:
                max_consec_count = max(max_consec_count, curr_consecutive_count)
                curr_consecutive_count = 1
        max_consec_count = max(curr_consecutive_count, max_consec_count)        
        return max_consec_count

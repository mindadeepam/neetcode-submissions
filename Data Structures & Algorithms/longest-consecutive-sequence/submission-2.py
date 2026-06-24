class Solution:
    def longestConsecutive_nlogn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        curr_consecutive_count = 1
        max_consec_count = 1
        n = len(nums)
        for e in range(1, n):
            if nums[e]-nums[e-1]==1:
                curr_consecutive_count += 1
            if nums[e]-nums[e-1]>1:
                max_consec_count = max(max_consec_count, curr_consecutive_count)
                curr_consecutive_count = 1
        max_consec_count = max(curr_consecutive_count, max_consec_count)        
        return max_consec_count

    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        
        max_consec = 0
        for num in hashmap:
            curr_consec = 0
            if num-1 not in hashmap:
                # then num is a start of new seq..
                # look till u dont get next num
                curr_consec += 1
                curr_num = num
                while curr_num+1 in hashmap:
                    curr_num += 1
                    curr_consec +=1
                max_consec = max(curr_consec, max_consec)
        

        return max_consec

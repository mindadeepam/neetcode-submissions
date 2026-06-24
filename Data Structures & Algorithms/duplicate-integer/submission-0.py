class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        count_arr = {}
        for i, num in enumerate(nums):
            if num in count_arr:
                return True
            count_arr[num]=1
        
        return False



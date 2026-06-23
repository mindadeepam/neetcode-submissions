from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_arr = [0]*3000
        for num in nums:
            count_arr[num+1000] += 1

        count_arr_with_indices = list(enumerate(count_arr))
        print(count_arr_with_indices)
        count_arr_with_indices = sorted(count_arr_with_indices, key=lambda x: x[1], reverse=True)
        return [i-1000 for i, val in count_arr_with_indices[:k]]
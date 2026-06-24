class Solution:
    def twoSum(self, nums, target):
        # nums is already sorted
        seen = []
        results = []
        for i, num in enumerate(nums):
            search_for = target - num
            if search_for in seen:
                results.append([num, search_for])
            else:
                seen.append(num)

        return results
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        target = 0
        triplets = list()
        for i, num in enumerate(nums):
            target_for_two_sum = target - num
            two_sum_result = self.twoSum(nums[i+1:], target_for_two_sum)
            for res in two_sum_result:
                triplets.append([num] + res)
        
        dist_trips = set()
        for triplet in triplets:
            hashable_trip = tuple(sorted(triplet))
            if hashable_trip in dist_trips:
                continue
            else:
                dist_trips.add(hashable_trip)

        
        return [list(trip) for trip in dist_trips]


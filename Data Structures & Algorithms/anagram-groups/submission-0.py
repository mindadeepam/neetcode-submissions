class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for i, item in enumerate(strs):
            sorted_item = "".join(sorted(item))
            if sorted_item in hashmap:
                hashmap[sorted_item].append(item)
            else:
                hashmap[sorted_item] = [item]

        return list(hashmap.values())
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,element in enumerate(nums):
            diff = target - element
            if diff in hashmap:
                return [hashmap[diff],index]
            hashmap[element] = index
        return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in hp:
                return [hp[diff], i]

            hp[v] = i

        return [-1, -1]
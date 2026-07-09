class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = []
        for i,v in enumerate(nums):
            if v in hm:
                return True
            hm.append(v)
        return False

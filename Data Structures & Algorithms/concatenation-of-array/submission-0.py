class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*2*n
        for i in range(n):
            ans[i + n] = nums[i]
            ans[i] = nums[i]

        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make it a set
        numSet = set(nums)
        count_max, count = 0, 0

        for num in numSet:
            if num-1 not in numSet:
                count = 1
                while num+count in numSet:
                    count += 1
                count_max = max(count_max, count)
        
        return count_max



       


            




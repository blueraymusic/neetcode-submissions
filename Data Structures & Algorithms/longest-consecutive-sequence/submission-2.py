class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #make it a set
        numset = set(nums)
        count_max = 0 
        count = 0 

        for num in numset:
            if num-1 not in numset:
                count = 1
                while num+count in numset:
                    count += 1
            count_max = max(count, count_max)  
        
        return count_max



            




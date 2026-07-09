class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {} 

        for index, val in enumerate(numbers):
            diff = target - val
            if diff in hmap:
                return [hmap[diff]+1, index+1]
            
            hmap[numbers[index]] = index
        
        return -1
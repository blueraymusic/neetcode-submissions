class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = {}
        res = []

        #O(n)
        for i,v in enumerate(nums):
            if v in r:
                r[v] +=1 
            else:
                r[v] =1 
        
        #return
        while k > 0:
            m = max(r, key=r.get)
            res.append(m)
            r[m] =0
            k -= 1 


        return res



        
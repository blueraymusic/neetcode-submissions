class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_mp = {}

        for i in nums:
            if i in h_mp:
                h_mp[i] += 1
            
            else:
                h_mp[i] = 1

        res = []


        while k > 0:
            m = max(h_mp.values())
            
            for key, value in h_mp.items():
                if m == value:
                    res.append(key)
                    h_mp[key] = 0
                    m = max(h_mp.values())
                    k -= 1

                    if k == 0:
                        break
            
        return res
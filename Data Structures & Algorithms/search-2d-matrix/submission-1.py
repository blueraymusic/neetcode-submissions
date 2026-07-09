class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Plan: filter rows, then binary search
        # 1) binary search 
        def binary_search(mat: list[int], find: int) -> bool:
            l,r = 0, len(mat)-1
            while l<=r:
                mid = (l+r) // 2 
                if mat[mid] == find:
                    return True
                elif mat[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False
        
        # 2) filtering 
        for vec in matrix:
            if  vec[0] <= target <= vec[-1]:
                return binary_search(vec, target)
        
        return False

        
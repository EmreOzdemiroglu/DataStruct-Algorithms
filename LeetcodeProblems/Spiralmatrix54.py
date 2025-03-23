class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            # 1) add first row/list of matrix
            # Example: if matrix = [[1,2,3],[4,5,6],[7,8,9]], we add [1,2,3] to ret
            # ret = [1,2,3], matrix becomes [[4,5,6],[7,8,9]]
            ret += (matrix.pop(0))
            
            # 2) append last element of all lists in matrix
            # Example: we take the last element of each remaining row
            # ret = [1,2,3,6,9], matrix becomes [[4,5],[7,8]]
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            
            # 3) add reverse of last row/list
            # Example: we add the last row in reverse order
            # ret = [1,2,3,6,9,8,7], matrix becomes [[4,5]]
            if matrix:
                ret += (matrix.pop())[::-1]
            
            # 4) append first element of all rows/lists
            # Example: we take the first element of each remaining row (bottom to top)
            # ret = [1,2,3,6,9,8,7,4], matrix becomes [[5]]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
                    
        return ret
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            # 1) add first row/list of matrix
            ret += (matrix.pop(0))
            
            # 2) append last element of all lists in matrix
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            
            # 3) add reverse of last row/list
            if matrix:
                ret += (matrix.pop())[::-1]
            
            # 4) append first element of all rows/lists
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
                    
        return ret
m
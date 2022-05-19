class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
            
        t = 0
        for i in range(len(mat)):
            t += mat[i][i]
            t += mat[i][len(mat)-i-1]
            
        if len(mat)%2 == 1:
                t -= mat[len(mat)/2][len(mat)/2]       
        return t
        

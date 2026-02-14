class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
        return transpose

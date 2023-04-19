class NumMatrix:
    """
    Approach 1: 2D Prefix Sum
    time: O(mn) for initializaion, O(1) for sumRegion()
    space: O(mn)
    Requirement: sumRegion() works on O(1) time complexity
    """
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.prefix

        for i in range(m):
            for j in range(n):
                _sums[i+1][j+1] = _sums[i][j+1] + _sums[i+1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.prefix
        return _sums[row2+1][col2+1] - _sums[row1][col2+1] - _sums[row2+1][col1] + _sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

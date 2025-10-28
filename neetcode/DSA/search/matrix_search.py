class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1
        while (L <= R):
            m = (L+R)//2
            m_low = matrix[m][0]
            m_high = matrix[m][-1]

            if target >= m_low and target <= m_high:

                return self.binarySearch(matrix[m], target)
            elif target < m_low:
                R = m - 1
            else:
                L = m + 1 
        return False

    

    def binarySearch(self, lst, target):
        L, R = 0, len(lst) - 1
        while L <= R:
            m = (L+R) // 2 
            if target < lst[m]:
                R -= 1
            elif target > lst[m]:
                L += 1
            else:
                return True
        return False
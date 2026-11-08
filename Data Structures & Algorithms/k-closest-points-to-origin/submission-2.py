class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    # Sort the matrix in-place based on the squared distance from the origin
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
    
    # Return the first K elements from the sorted matrix
        return points[:k]

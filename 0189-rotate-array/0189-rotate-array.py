from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        test = deque(nums)
        test.rotate(k)
        
        nums.clear()
        [nums.append(i) for i in test]
        
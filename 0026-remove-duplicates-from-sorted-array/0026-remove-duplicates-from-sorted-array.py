class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 배열을 다시 할당하지 않는 것이 중요함
        nums[:] = sorted(set(nums))
        return len(nums)
        
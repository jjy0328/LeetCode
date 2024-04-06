# Time Limit Exceeded
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         # 첫 번째 높이부터 시작하여 각 높이에 대해 반복
#         for i in range(len(height)):
#             # 현재 높이보다 오른쪽에 있는 모든 높이에 대해 반복
#             for j in range(i+1, len(height)):
#                 # 최대 면적을 현재 면적과 비교하여 더 큰 값으로 갱신
#                 max_area = max(max_area, min(height[i], height[j]) * (j - i))
#         return max_area

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        max_area=0
        
        while(right-left>0):
            max_area=max(max_area, (right-left)*min(height[left], height[right]))
            
            if height[left]>=height[right]: # The right is shorter than left
                right-=1
            else: # The left is shorter than right
                left+=1
        
        return max_area
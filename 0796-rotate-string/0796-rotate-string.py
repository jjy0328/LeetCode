class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s == goal:
            return True
        
        for i in range(len(s)):
            back = s[:i]
            front = s[i:]
            if (front+back) == goal:
                return True
        
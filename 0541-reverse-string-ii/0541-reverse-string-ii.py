class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        
        for i in range(0, len(s), 2*k):
            list_s[i:i+k] = list_s[i:i+k][::-1]

        return "".join(list_s)
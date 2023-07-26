class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = list(str(x))
        reverse_lst =lst[::-1]
        if lst == reverse_lst:
            return True
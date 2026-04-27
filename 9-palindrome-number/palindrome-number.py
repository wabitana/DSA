class Solution:
    def isPalindrome(self, x: int) -> bool:
        xst=str(x)
        if xst == xst[::-1]:
            return True
        return False
        
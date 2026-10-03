class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  "".join(char.lower() for char in s if char.isalnum())
        return list(s) == list(s)[::-1]
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =  "".join(char.lower() for char in s if char.isalnum())
        list1 = list(s)
        list2 = list1[-1:-len(list1) - 1:-1]
        return list1 == list2
        
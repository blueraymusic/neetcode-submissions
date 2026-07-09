class Solution:
    def isPalindrome(self, s: str) -> bool:
        se = ""
        for n in s:
            if n.isalnum():
                se += n
        return (se.strip().lower()) == (se.strip().lower())[::-1]
#THIS IS #125 QUESTION IN LEETCODE
#FROM THIS QUESTION I LEARNT ABOUT REMOVING NON ALPHANUMERIC CHARACTERS

class Solution:
    def isPalindrome(self, s: str):
        cleaned=""
        for char in s:
            if char.isalnum():
                cleaned=cleaned+char.lower()
        rev=cleaned[::-1]
        if cleaned==rev:
            return True
        else:
            return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif len(s) == 1:
            return 1

        left = 0
        right = 1
        length = 0
        while right < len(s):
            if s[right] in s[left:right]:
                left = left + s[left:right].index(s[right]) + 1
            length = max(right - left + 1, length)
            right += 1
        return length
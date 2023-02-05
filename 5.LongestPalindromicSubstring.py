class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(0, len(s)):
            left = i
            right = i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            len1 = right - left - 1
            left = i
            right = i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            len2 = right - left - 1
            length = max(len1, len2)
            if length > end - start:
                start = i - ((length - 1) // 2)
                end = i + length // 2
        return s[int(start):int(end + 1)]
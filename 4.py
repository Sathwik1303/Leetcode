#THIS IS #4 QUESTION IN LEETCODE
#SO FROM THIS QUESTION I LEARNT WHERE TO USE // AND / OPERATORS

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        
        if n % 2 == 0:
            left = merged[n//2 - 1]
            right = merged[n//2]
            return (left + right) / 2
        else:
            return merged[n // 2]
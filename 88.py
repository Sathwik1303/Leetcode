#MERGING SORTED ARRAY

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ans=[] 
        for i in range(0,m):
            ans.append(nums1[i])
        for j in range(0,n):
            ans.append(nums2[j])
        ans.sort()
        nums1[:]=ans
        return nums1           
        
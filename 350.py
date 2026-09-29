#INTERSECTION OF TWO ARRAYS II

class Solution(object):
    def intersect(self, nums1, nums2):
        new=[]
        for i in nums1:
            if i in nums2:
                new.append(i)
                nums2.remove(i)
        return new        
#SHUFFLE AN ARRAY

import random
class Solution(object):

    def __init__(self, nums):
        self.nums=nums[:]
        self.old=nums[:]
        

    def reset(self):
        self.old=self.nums[:]
        return self.old
        

    def shuffle(self):
        random.shuffle(self.old)
        return self.old
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
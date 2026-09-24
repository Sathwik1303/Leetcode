#SMALLEST INDEX WITH DIGIT SUM EQUAL TO INDEX

class Solution(object):
    def smallestIndex(self, nums):
        v = 0
        for i in range(0, len(nums)):
            n = nums[i]
            digit_sum = 0
            while n > 0:
                digit_sum += n % 10
                n //= 10
            if i == digit_sum:
                v = 1
                return i
        if v == 0:
            return -1
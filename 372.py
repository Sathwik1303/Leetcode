#SUPER POW

class Solution(object):
    def superPow(self, a, b):
        if a==1:
            return 1
        MOD=1337
        ans=1
        for i in b:
            part1=pow(ans,10,MOD)
            part2=pow(a,i,MOD)
            ans=(part1*part2)%MOD
        return ans    
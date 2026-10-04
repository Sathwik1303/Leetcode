#MULTIPLICATION OF COMPLEX NUMBERS

class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        a, b = map(int, num1[:-1].split("+"))
        c, d = map(int, num2[:-1].split("+"))
        return f"{a*c - b*d}+{a*d + b*c}i"
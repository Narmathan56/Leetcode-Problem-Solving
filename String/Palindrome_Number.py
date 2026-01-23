class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        word = ""

        for i in range(len(x) - 1, -1, -1):
            word += x[i]

        return word == x

#Problem:Longest Palindrome Substring
#Mode:Medium
#Method: Dynamic Progrmming
#Profile:https://leetcode.com/u/Narmathan26/


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

       # HI, Today, I am gonna Solve the Longest Palindrome Subsring In Word
       #Let's Start



    # i am gonna read properly then i will understand it first
    # this must be String
    # S would be a digits and english letters
    #babad----->bab or aba 
    #cbbd------->bb
    #here i can tell approximatley  if that word length is in odd number, we need to insert the if statement to devide as even or odd, and 2 for loop for create the substring and one for loop for check is that palindrome or not. so Time complexity is O(n**2) for first for loop and O(n) for last forloop(checking) so totally,O(n**3)


    #1 function to define the sub for checking reverse
         # this reverse the sub by ::-1 for instace aba and if that reverse string is true return the sub to check the conditon and return the longest with compare the max_len

       
    # Overall This is called Brute force

    # This is used to Check all possiblities and choose right one from all of the posiblities this is time complexity is O(n**3) so n increase fastly, so this is not suitable for larger inputs




    ## Now I am gonna try the Dynamic programming and show how efficient that is:)


        n=len(s)
        if n==0:
          return ""# edge case


    # dp start

        dp=[[False]*n for _ in range(n)]
        start=0
        max_len=1
    #base case start
        for i in range(n):# checking single charcters
            dp[i][i]=True 

        for length in range(2,n+1):# 2 is minimum length of substring and n+1 is j-1
            for i in range(n-length+1):# this is range for instance if i give the n=5 and length=2 the word ="bababa" so (5-2+1)= range(4) that substring creation until that range if that over range  overflow that's why this method

                    j=i+length-1 # so here is actual substring creation happening.i=0 length 2 so calculation j=0+2-1
                    if s[i]==s[j]: # here this will check the i=0 and s=1 is same or not                   
                        if length==2 or dp[i+1][j-1]:
                            dp[i][j]=True
                            if length>max_len:
                               start=i
                               max_len=length
        return s[start:start+max_len]   

Time complexity: O(n**2)

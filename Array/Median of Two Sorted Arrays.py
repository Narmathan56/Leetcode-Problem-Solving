#problem:Median of Two Sorted Arrays
#Mode: Hard
#Complexity: O(log(Min(M,n)))
#Algorithm Used: Binary Search
#LeetCode Profile: https://leetcode.com/u/Narmathan26/





class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # this is wrong because it use the O(n**2). According to this problem we have to attain the O(log(m+n)). so this is crucial. we are gonna use binary search instead of sorting and devide and get the I am gonna comment this
        
        if len(nums1)>len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len1=len(nums1)
        len2=len(nums2)
        left=0
        right=len1


        while left<=right:
            part1=(left+right)//2
            part2=(len1+len2+1)//2-part1

            max_left1=float('-inf')if part1==0 else nums1[part1-1]
            min_right1=float('inf')if part1==len1 else nums1[part1]
            max_left2=float('-inf')if part2==0 else nums2[part2-1]
            min_right2=float('inf')if part2==len2 else nums2[part2]


            if max_left1<=min_right2 and max_left2<=min_right1:
                if (len1+len2)%2==0:
                    return (max(max_left1,max_left2)+min(min_right1,min_right2))/2.0
                else:
                    return max(max_left1,max_left2)
            elif max_left1>min_right2:
                right=part1-1
            else:
                left=part1+1                

        


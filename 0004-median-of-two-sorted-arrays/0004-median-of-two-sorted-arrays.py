class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=[]
        b=[]
        a=nums1+nums2
        a.sort()
        if len(a)%2==0:

            return (float(a[len(a)//2]+a[(len(a)-1)//2])/2)
        else:
            return (float(a[len(a)//2]))

        
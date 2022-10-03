class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #if it has only one element
        if len(nums)==1:
            return 0
            
         #assigning low value to zero
        l=0
        #assigning high value to last value (here one less then length as index starts from 0)
        h=len(nums)-1
         
        #continue until low is less than or equal high
        while l<=h:
            #finding the mid value with integer overflow check
            mid=l+(h-l)//2
            
            
            #checking whether the selected element is peak element
            #aslso checking the out of bound conditon in mid==0 and mid==0
            if (mid==0 or nums[mid-1]<nums[mid]) and (mid==len(nums)-1 or nums[mid+1]<nums[mid]):
                #then return the mid index
                return mid
            
            #if the previous value of mid is greater 
            elif ( mid >0 and nums[mid-1]>nums[mid]):
                #assigning high value to mid -1
                h=mid -1
               #if the next value id greater then mid element
            else:
                l=mid+1
        
        return 
                
                
                
                
                
        
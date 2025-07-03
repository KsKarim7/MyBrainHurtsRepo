class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if(nums[i] == 0):
                j = i+1
                while(j<len(nums)):
                    if(nums[j] != 0):
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
                    j+=1

                    

        return nums
        
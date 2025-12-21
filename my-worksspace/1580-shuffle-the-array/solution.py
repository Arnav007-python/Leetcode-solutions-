class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n):
            # Append xi (from the first half)
            result.append(nums[i])
            # Append yi (from the second half, located at i + n)
            result.append(nums[i + n])
        return result
        

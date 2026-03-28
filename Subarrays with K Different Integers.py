class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k_max):
            freq ={}
            left = 0
            total_subarrays = 0
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1
                while len(freq) > k_max:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                total_subarrays += right - left + 1
            return total_subarrays
        return atMost(k) - atMost(k - 1)
                

            

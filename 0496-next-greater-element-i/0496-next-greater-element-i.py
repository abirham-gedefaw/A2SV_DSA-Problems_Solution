class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = defaultdict(lambda: -1)
        m, n = len(nums1), len(nums2)

        for i in range(n):
            for j in range(i +1, n):
                if nums2[j] > nums2[i]:
                    res[nums2[i]] = nums2[j]
                    break
        return [res[nums1[i]] for i in range(m)]
        
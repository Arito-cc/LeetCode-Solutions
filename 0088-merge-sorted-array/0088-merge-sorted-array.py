class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1  # real end index of num1
        j = n - 1  # real end indec of num2
        k = m + n - 1  # end of num1

        while j >= 0:
            if i < 0:
                nums1[k] = nums2[j]
                j-=1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1

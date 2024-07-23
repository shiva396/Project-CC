class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = sorted(sorted(nums,reverse = True), key = lambda x : nums.count(x))
        return nums
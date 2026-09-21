class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k%=len(nums)
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
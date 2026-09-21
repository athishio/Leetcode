class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n=len(nums)
        k%=n
        def r(a,b):
            while a<b:
                nums[a],nums[b]=nums[b],nums[a]
                a+=1
                b-=1
        r(0,n-1)
        r(0,k-1)
        r(k,n-1)
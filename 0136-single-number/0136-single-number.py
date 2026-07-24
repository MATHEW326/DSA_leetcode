class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=0
        for i in range(len(nums)):
            x=x^nums[i]
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
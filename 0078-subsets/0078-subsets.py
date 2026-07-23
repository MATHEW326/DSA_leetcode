import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        subset=[]
        n=len(nums)
        def backtrack(subset,start):
            results.append(subset[:])
            for i in  range(start,n):
                subset.append(nums[i])
                backtrack(subset,i+1)
                subset.pop()

        backtrack([],0)
        return results



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
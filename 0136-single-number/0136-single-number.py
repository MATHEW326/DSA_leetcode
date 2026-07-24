class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary={}
        x=-1
        for i in nums:
            dictionary[i]=dictionary.get(i,0)+1
        for k,v in dictionary.items():
            if v==1:
                return k
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dictionary={}
        x=0
        for i in nums:
            dictionary[i]=dictionary.get(i,0)+1
        for key,val in dictionary.items():
            if val==2:
                x=x^key
        print(dictionary)
        return x


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
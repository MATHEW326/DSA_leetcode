class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        arr=[0]*(n+1)
        arr[0]=0
        arr[1]=1
        arr[2]=2
        for i in range(3,n+1):
            arr[i]=arr[i-1]+arr[i-2]


        return arr[n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
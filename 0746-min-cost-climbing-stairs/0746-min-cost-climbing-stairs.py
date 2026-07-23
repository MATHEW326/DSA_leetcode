class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store={}
        def rec(i):
            if i==0 or i==1:
                return 0
            if i in store:
                return store[i]
            store[i]=min(rec(i-1)+cost[i-1],rec(i-2)+cost[i-2])
            return store[i]
        return rec(len(cost))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
from collections import defaultdict,deque
class Solution(object):
    def bfs(self,i,visited,adjlist):
        queue=deque([i])
        while len(queue)!=0:
            current_node=queue.popleft()
            for neighbor in adjlist[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor]=1
        
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        cnt=0
        visited=[0]*len(isConnected)
        adjlist=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and i!=j:
                    adjlist[i].append(j)
                    adjlist[j].append(i)
        for i in range(len(isConnected)):
            if not visited[i]:
                cnt+=1
                self.bfs(i,visited,adjlist)
        return cnt
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
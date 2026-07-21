from collections import defaultdict
from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[Lmist[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj_list=defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited=set()
        queue=deque([source])
        while len(queue)!=0:
            current_node=queue.popleft()
            if current_node==destination:
                return True
            for neighbor in adj_list[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False
        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
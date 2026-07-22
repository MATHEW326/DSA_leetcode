from collections import deque

class Solution(object):
    def bfs(self,grid,r,c,visited):
        queue=deque()
        queue.append([r,c])
        visited[r][c]=1
        while len(queue)!=0:
            row_val,col_val=queue.popleft()
            for i in range(-1,2):
                for j in range(-1,2):
                    if abs(i) + abs(j) != 1:
                        continue
                    curr_row=i+row_val
                    curr_col=j+col_val
                    m=len(grid)
                    n=len(grid[0])
                    if curr_row>=0 and curr_row<m and curr_col>=0 and curr_col<n and grid[curr_row][curr_col]=='1' and not visited[curr_row][curr_col]:
                        
                        queue.append((curr_row,curr_col))
                        visited[curr_row][curr_col]=1


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        visited=[[0 for _ in range(col)] for _ in range(row)]
        count=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and not visited[r][c]:
                    count+=1
                    self.bfs(grid,r,c,visited)
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
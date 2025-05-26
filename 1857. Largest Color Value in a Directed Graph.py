from collections import deque, defaultdict

class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # dp[node][color] = max count of this color along any path ending at node
        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][ord(colors[i]) - ord('a')] = 1

        processed = 0
        res = 0

        while queue:
            node = queue.popleft()
            processed += 1
            for nei in graph[node]:
                for c in range(26):
                    dp[nei][c] = max(dp[nei][c], dp[node][c] + (1 if c == ord(colors[nei]) - ord('a') else 0))
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
            res = max(res, max(dp[node]))

        return res if processed == n else -1
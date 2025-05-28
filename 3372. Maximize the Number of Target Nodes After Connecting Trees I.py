from collections import deque

class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        """
        :type edges1: List[List[int]]
        :type edges2: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        def buildAdjacencyList(edges, n):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def calculateReachableNodes(tree, n, k):
            reachable = [0] * n

            def bfs(start):
                visited = [False] * n
                queue = deque([(start, 0)])
                count = 0
                while queue:
                    node, dist = queue.popleft()
                    if visited[node] or dist > k:
                        continue
                    visited[node] = True
                    count += 1
                    for neighbor in tree[node]:
                        if not visited[neighbor]:
                            queue.append((neighbor, dist + 1))
                return count

            for i in range(n):
                reachable[i] = bfs(i)
            return reachable

        n, m = len(edges1) + 1, len(edges2) + 1
        tree1 = buildAdjacencyList(edges1, n)
        tree2 = buildAdjacencyList(edges2, m)

        reachable1 = calculateReachableNodes(tree1, n, k)
        reachable2 = calculateReachableNodes(tree2, m, k - 1)
        vaslenorix = [0] * n
        maxReachableInTree2 = max(reachable2)
        for i in range(n):
            vaslenorix[i] = reachable1[i] + maxReachableInTree2
        return vaslenorix
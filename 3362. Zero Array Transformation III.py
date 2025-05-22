class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        import heapq

        n = len(nums)
        m = len(queries)

        queries_by_start = [[] for _ in range(n)]
        for i, (l, r) in enumerate(queries):
            queries_by_start[l].append((r, i))

        available = []
        active = []
        used_count = 0

        for pos in range(n):
            for end_pos, query_idx in queries_by_start[pos]:
                heapq.heappush(available, (-end_pos, query_idx))

            while active and active[0][0] < pos:
                heapq.heappop(active)

            current_coverage = len(active)
            need_more = nums[pos] - current_coverage

            if need_more > 0:
                for _ in range(need_more):
                    found = False
                    temp_removed = []

                    while available:
                        neg_end, query_idx = heapq.heappop(available)
                        end_pos = -neg_end

                        if end_pos >= pos:
                            heapq.heappush(active, (end_pos, query_idx))
                            used_count += 1
                            found = True
                            break
                        else:
                            temp_removed.append((neg_end, query_idx))

                    for item in temp_removed:
                        heapq.heappush(available, item)

                    if not found:
                        return -1

        return m - used_count
from collections import deque


class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        n = len(status)
        queue = deque()
        has_key = set()
        seen = set()
        to_process = set(initialBoxes)

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
                seen.add(box)
            else:
                # If closed, we wait until we get the key
                pass

        candies_collected = 0

        while queue:
            box = queue.popleft()
            candies_collected += candies[box]

            # Add new keys
            for key in keys[box]:
                if key not in has_key:
                    has_key.add(key)
                    if key in to_process and key not in seen:
                        queue.append(key)
                        seen.add(key)

            # Add contained boxes
            for new_box in containedBoxes[box]:
                if new_box not in seen:
                    to_process.add(new_box)
                    if status[new_box] == 1 or new_box in has_key:
                        queue.append(new_box)
                        seen.add(new_box)

        return candies_collected
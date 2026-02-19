class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for i, (x1, y1) in enumerate(points):
            distance_count = {}
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                dx = x1 - x2
                dy = y1 - y2
                distance = dx * dx + dy * dy
                distance_count[distance] = distance_count.get(distance, 0) + 1

            for count in distance_count.values():
                total += count * (count - 1)
        return total

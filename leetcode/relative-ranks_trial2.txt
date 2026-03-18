class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = [(s, i) for i, s in enumerate(score)]
        pairs.sort(reverse = True, key = lambda x: x[0])
        print(pairs)
        result = [""] * len(score)
        for rank, (_,index) in enumerate(pairs):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)
        return result



        
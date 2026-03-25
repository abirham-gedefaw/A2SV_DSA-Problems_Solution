class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_w_count = blocks[:k].count("W")
        min_recolor = curr_w_count
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                curr_w_count += 1
            if blocks[i - k] == "W":
                curr_w_count -= 1
            min_recolor = min(min_recolor, curr_w_count)
        return min_recolor



          
        
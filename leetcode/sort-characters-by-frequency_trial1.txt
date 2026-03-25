class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_items = counter.most_common()
        return "".join(char * freq for char, freq in sorted_items)

        
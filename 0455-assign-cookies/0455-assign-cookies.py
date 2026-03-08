class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookie = 0
        content = 0
        g.sort()
        s.sort()
        while content < len(g) and cookie < len(s):
            if s[cookie] >= g[content]:
                content += 1
            cookie += 1

        return content

        
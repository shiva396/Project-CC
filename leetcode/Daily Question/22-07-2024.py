class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for j in zip(names, heights):
            l.append(j)
        l.sort(key = lambda x : x[-1], reverse = True)
        j = list(map(lambda x : x[0],l))
        return j
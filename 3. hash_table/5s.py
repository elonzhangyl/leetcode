class Solution:
    def founder(self, lst: list[int], target: int) -> list[int]:
        record = {}
        for index, value in enumerate(lst):
            if target-value in record:
                return [record[target-value], index]
            record[value] = index
        return []

Solution().founder([1,2,3,4],5)

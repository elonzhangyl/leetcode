# [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# ["JFK", "MUC", "LHR", "SFO", "SJC"]
from collections import defaultdict
class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def trip(self, tickets):
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
        for airport in tickets_dict:
            tickets_dict[airport].sort()
        self.backtracking(tickets, 'JFK')
        return self.res

    def backtracking(self, tickets, start):
        if len(tickets) == 0:
            self.res.append(self.path[:])
            return True

        for i in range(len(tickets)):
            if tickets[i][0] == start:
                self.path.append(tickets[i])
                if self.backtracking(tickets[0:i] + tickets[i + 1:], tickets[i][1]):
                    return True
                self.path.pop()

print(Solution().trip([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

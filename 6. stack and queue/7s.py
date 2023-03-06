from collections import deque


class myQueue:
    def __init__(self) -> None:
        self.q = deque()

    def pop(self, e):
        if self.q and self.q[0] == e:
            self.q.popleft()

    def push(self, e):
        while self.q and e > self.q[-1]:
            self.q.pop()
        self.q.append(e)

    def windowMax(self):
        return self.q[0]
    
    

class Solution():
    def slidingWindowMax(self, lst: list[int], k: int) -> list[int]:
        q = myQueue()
        res = []
        for i in range(k):
            q.push(lst[i])
        res.append(q.windowMax())
        for i in range(k, len(lst)):
            q.pop(lst[i - k])
            q.push(lst[i])
            res.append(q.windowMax())
        return res


Solution().slidingWindowMax([1,3,-1,-3,5,3,6,7], 3)
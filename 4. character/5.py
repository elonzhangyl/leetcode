class Solution:
    def reverseList(self, lst: list[str]) -> None:
        left, right = 0, len(lst) - 1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return None

    def leftRotation(self, lst: list[str], loc: int) -> None:
        l1 = lst[:loc]
        self.reverseList(l1)
        self.reverseList(lst[loc:])
        self.reverseList(lst)
        return ''.join(lst)

print(Solution().leftRotation(list("abcdefghi"), 6))
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        start = 0
        end = len(people) - 1
        while start <= end:
            if people[start] + people[end] <= limit:
                res += 1
                start += 1
                end -= 1
            else:
                res += 1
                end -= 1
        return res
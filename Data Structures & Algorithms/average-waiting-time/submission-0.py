class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = []
        for i in range(len(customers)):
            arrival, waiting = customers[i]
            if not res or res[-1][0] < arrival:
                res.append([arrival+waiting, arrival + waiting - arrival])
            else:
                res.append([res[-1][0] + waiting, res[-1][0] + waiting - arrival])
        return sum([item[1] for item in res]) / len(res)
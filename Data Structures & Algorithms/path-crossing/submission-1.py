class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        points = {(x,y): 'start'}
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1
            tup = (x,y)
            if tup not in points:
                points[tup] = direction
            else:
                return True
        return False

from numpy import sign
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids = deque(asteroids)
        stack = []
        while asteroids:
            asteroid = asteroids.popleft()
            while stack and asteroid < 0 < stack[-1]:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
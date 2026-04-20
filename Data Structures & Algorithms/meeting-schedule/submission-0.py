"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))
        i = 0
        while i < len(intervals) - 1:
            current = intervals[i]
            if intervals[i+1].start < current.end:
                return False
            i += 1
        return True

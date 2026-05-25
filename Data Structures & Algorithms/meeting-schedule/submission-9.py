"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda meeting:meeting.start)
        previous_meeting_end = 0
        for interval in intervals:
            current_meeting_end = interval.end
            #compare the start time of the current meeting with the
            #end time of the previous meeting
            if interval.start < previous_meeting_end:
                return False
            previous_meeting_end = current_meeting_end
        return True

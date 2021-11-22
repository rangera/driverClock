from typing import List

from .clock_event import Event

class Summary():
    time_violation_limits = {'D': 11*60,
                             'W': 14*60}
    work_types = {'D': ['D'],
                  'W': ['D','W','OFF']}

    def __init__(self, type: str, events: List[Event]) -> None:
        if type not in self.work_types:
            raise ValueError(type + 'is not a valid Summary Type')

        self.type = type
    
        self.time_value = sum(event.time 
                                for event in events 
                                if event.work_status in self.work_types[self.type])

        self.violation_status = self.time_value > self.time_violation_limits[self.type]
   
    def to_json(self):
        return {'type': self.type,
                'violation_status': self.violation_status,
                'time_value': self.time_value}
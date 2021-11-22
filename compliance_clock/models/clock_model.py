from typing import List

from .event_model import Event

class Clock():
    time_violation_limits = {'D': 11*60,
                             'W': 14*60}
    work_types = {'D': ['D'],
                  'W': ['D','W','OFF']}

    violation_status = False

    def __init__(self, type: str, events: List[Event]) -> None:
        if type not in self.work_types:
            raise ValueError(type + 'is not a valid Summary Type')

        self.type = 'DRIVE_CLOCK' if type == 'D' else 'WORK_CLOCK'
    
        self.time_value = sum(event.time 
                                for event in events 
                                if event.work_status in self.work_types[type])

        self.violation_status = self.time_value > self.time_violation_limits[type]
   
    def to_json(self):
        return {'type': self.type,
                'violation_status': 'V' if self.violation_status else 'OK',
                'time_value': self.time_value}
# from typing import List

from flask import g

class Event():

    def __init__(self, work_status: str, time: int) -> None:
        self.work_status = work_status
        self.time = time

    def save(self):
        if not g.events:
            g.events = []
        g.events.append(self)
        
    def to_json(self):
        return {"work_status": self.work_status,
                "time": self.time}

    def objects():
        return g.events
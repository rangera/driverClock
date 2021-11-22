class Event():

    def __init__(self, work_status: str, time: int) -> None:
        self.work_status = work_status
        self.time = time
        
    def to_json(self):
        return {'work_status': self.work_status,
                'time': self.time}

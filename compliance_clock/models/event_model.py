class Event():

    def __init__(self, work_status: str, time: int) -> None:
        if work_status not in ['D','W','OFF']:
            raise ValueError(type + 'is not a valid work status')

        self.work_status = work_status
        self.time = time
        
    def to_json(self):
        return {'work_status': self.work_status,
                'time': self.time}

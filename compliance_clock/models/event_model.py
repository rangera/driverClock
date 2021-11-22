class Event():

    def __init__(self, work_status: str, time: int) -> None:
        if work_status not in ['D','W','OFF']:
            raise ValueError(type + 'is not a valid work status')

        if not (0 <= time and time <= 365*24*60):
            raise ValueError(
                'Time must be a positive integer (of minutes) less than the minutes in a year')

        self.work_status = work_status
        self.time = time
        
    def to_json(self):
        return {'work_status': self.work_status,
                'time': self.time}

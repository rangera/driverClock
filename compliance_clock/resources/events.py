
from ..db import get_db
from ..models import Event

from typing import List

def save_event(event: Event):
    db = get_db()
    db.execute('INSERT INTO events (work_status, time_duration) VALUES (?, ?)',
        (event.work_status, event.time),)
    db.commit()

def get_all_events() -> List[Event]:
    db = get_db()
    rows = db.execute(
        'SELECT work_status, time_duration FROM events'
    ).fetchall()
    return [Event(row['work_status'], row['time_duration']) for row in rows]
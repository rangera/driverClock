import pytest

from compliance_clock.models import Clock
from compliance_clock.models import Event

def test_create():
    c = Clock(type='D',events=[])
    assert c is not None
    c = Clock(type='W',events=[])
    assert c is not None
    assert [key for key in c.to_json().keys()] == [
        'type',
        'violation_status',
        'time_value',
    ]

def test_create_invalid():
    with pytest.raises(ValueError):
        Clock(type='not_registered_clock_type',events=[])
    
def test_drive_clock_events():
    events = [Event(work_status, time) for (work_status, time) in [
        ('D', 30),
        ('W', 30)
    ]]
    c = Clock(type='D', events=events)
    assert c.time_value == 30

def test_drive_clock_validation():
    events = [Event(work_status, time) for (work_status, time) in [
        ('D', 11*60)
    ]]
    c = Clock(type='D', events=events)
    assert c.violation_status is False
    events.append(Event('D', 1))
    c = Clock(type='D', events=events)
    assert c.violation_status is True


def test_work_clock_events():
    events = [Event(work_status, time) for (work_status, time) in [
        ('W', 30),
        ('D', 30),
        ('OFF', 30),
        ('W', 30),
    ]]
    c = Clock(type='W', events=events)
    assert c.time_value == 120

def test_work_clock_validation():
    events = [Event(work_status, time) for (work_status, time) in [
        ('W', 1*60),
        ('OFF', 1*60),
        ('D', 10*60),
        ('W', 2*60),
    ]]
    c = Clock(type='W', events=events)
    assert c.violation_status is False
    events.append(Event('W', 1))
    c = Clock(type='W', events=events)
    assert c.violation_status is True

@pytest.mark.parametrize('events,drive_clock_expectations,work_clock_expectations', [
    (
        [('D',120),('W',60),('OFF',30)],
        {'time':120, 'status':'OK'},
        {'time':3.5*60, 'status':'OK'}
    ),
    ( # requires shift reset
        [('D',120),('W',60),('OFF',11*60)],
        {'time':0, 'status':'OK'},
        {'time':0, 'status':'OK'}
    ),
    (
        [('D',120),('W',600),('D',180)],
        {'time':300, 'status':'OK'},
        {'time':15*60, 'status':'V'}
    ),
    (
        [('D',120),('OFF',9*60),('D',120)],
        {'time':240, 'status':'OK'},
        {'time':13*60, 'status':'OK'}
    ),
])
def test_clock_examples(events, drive_clock_expectations, work_clock_expectations):
    events = [Event(work_status, time) for (work_status, time) in events]
    
    drive_clock = Clock('D', events).to_json()
    work_clock = Clock('W', events).to_json()
    assert drive_clock['time_value'] == drive_clock_expectations['time']
    assert drive_clock['violation_status'] == drive_clock_expectations['status']
    assert work_clock['time_value'] == work_clock_expectations['time']
    assert work_clock['violation_status'] == work_clock_expectations['status']
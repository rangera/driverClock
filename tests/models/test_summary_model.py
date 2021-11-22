import pytest

from compliance_clock.models import Summary
from compliance_clock.models import Event

def test_create():
    s = Summary(type='D',events=[])
    assert s is not None
    s = Summary(type='W',events=[])
    assert s is not None

def test_create_invalid():
    with pytest.raises(ValueError):
        Summary(type='not_registered_summary_type',events=[])
    
def test_drive_clock_events():
    events = [Event(work_status, time) for (work_status, time) in [
        ('D', 30),
        ('W', 30)
    ]]
    s = Summary(type='D', events=events)
    assert s.time_value == 30

def test_drive_clock_validation():
    events = [Event(work_status, time) for (work_status, time) in [
        ('D', 11*60)
    ]]
    s = Summary(type='D', events=events)
    assert s.violation_status is False
    events.append(Event('D', 1))
    s = Summary(type='D', events=events)
    assert s.violation_status is True


def test_work_clock_events():
    events = [Event(work_status, time) for (work_status, time) in [
        ('W', 30),
        ('D', 30),
        ('OFF', 30),
        ('W', 30),
    ]]
    s = Summary(type='W', events=events)
    assert s.time_value == 120

def test_work_clock_validation():
    events = [Event(work_status, time) for (work_status, time) in [
        ('W', 1*60),
        ('OFF', 1*60),
        ('D', 10*60),
        ('W', 2*60),
    ]]
    s = Summary(type='W', events=events)
    assert s.violation_status is False
    events.append(Event('W', 1))
    s = Summary(type='W', events=events)
    assert s.violation_status is True

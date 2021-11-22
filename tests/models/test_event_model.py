from compliance_clock.models import Event

def test_create():
    e = Event(work_status='D',time=30)
    assert e is not None
    assert e.work_status == 'D'
    assert e.time == 30
    assert e.to_json() == {'work_status': e.work_status,
                           'time': e.time}


# from flask import g

from compliance_clock.models import Event

def test_create():
    e = Event(work_status='D',time=30)
    assert e is not None

# def test_save():
#     e = Event(work_status='D',time=30)
#     assert not g.events
#     e.save()
#     assert g.events == [e]


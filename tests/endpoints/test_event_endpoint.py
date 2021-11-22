import json

from flask import g

from compliance_clock.resources.events import get_all_events

def test_put_single_event(client):
    with client:
        r = client.put('/event', 
            data=json.dumps({'work_status': 'D','time': 30}))
        
        response = json.loads(r.data)
        assert response['work_status'] == 'D'
        assert response['time'] == 30

        events = get_all_events()
        assert len(events) == 1
        assert events[0].work_status == 'D'
        assert events[0].time == 30

def test_put_multiple_events(client):
    with client:
        r = client.put('/event', 
            data=json.dumps({'work_status': 'W','time': 60}))
        
        events = get_all_events()
        assert len(events) == 1
        assert events[0].work_status == 'W'
        assert events[0].time == 60

        r = client.put('/event', 
            data=json.dumps({'work_status': 'D','time': 30}))
        
        response = json.loads(r.data)
        assert response['work_status'] == 'D'
        assert response['time'] == 30

        events = get_all_events()
        assert len(events) == 2
        assert events[0].work_status == 'W'
        assert events[0].time == 60
        assert events[1].work_status == 'D'
        assert events[1].time == 30

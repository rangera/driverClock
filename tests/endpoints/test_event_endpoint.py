from flask import g
import json

def test_put_single_event(client):
    with client:
        r = client.put('/event', 
            data=json.dumps({'work_status': 'D','time': 30}))
        
        response = json.loads(r.data)
        assert response['work_status'] == 'D'
        assert response['time'] == 30

        assert len(g.events) == 1
        assert g.events[0].work_status == 'D'
        assert g.events[0].time == 30

def test_put_multiple_events(client):
    with client:
        r = client.put('/event', 
            data=json.dumps({'work_status': 'W','time': 60}))
        
        assert len(g.events) == 1
        assert g.events[0].work_status == 'W'
        assert g.events[0].time == 60

        r = client.put('/event', 
            data=json.dumps({'work_status': 'D','time': 30}))
        
        response = json.loads(r.data)
        assert response['work_status'] == 'D'
        assert response['time'] == 30

        assert len(g.events) == 2
        assert g.events[0].work_status == 'W'
        assert g.events[0].time == 60
        assert g.events[1].work_status == 'D'
        assert g.events[1].time == 30

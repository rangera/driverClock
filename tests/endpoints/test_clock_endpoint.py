import json

import pytest
from flask import g

from compliance_clock.models import Event

def test_blank_clocks(client):
    with client:
        r = client.get('/clock')
        response = json.loads(r.data)

        assert response[0]['type'] == 'DRIVE_CLOCK'
        assert response[0]['time_value'] == 0
        assert response[0]['violation_status'] == 'OK'

        assert response[1]['type'] == 'WORK_CLOCK'
        assert response[1]['time_value'] == 0
        assert response[1]['violation_status'] == 'OK'

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

def test_example_clocks(client, events, drive_clock_expectations, work_clock_expectations):
    with client:
        
        g.events = [Event(work_status, time) for (work_status, time) in events]

        r = client.get('/clock')
        response = json.loads(r.data)

        assert response[0]['type'] == 'DRIVE_CLOCK'
        assert response[0]['time_value'] == drive_clock_expectations['time']
        assert response[0]['violation_status'] == drive_clock_expectations['status']

        assert response[1]['type'] == 'WORK_CLOCK'
        assert response[1]['time_value'] == work_clock_expectations['time']
        assert response[1]['violation_status'] == work_clock_expectations['status']

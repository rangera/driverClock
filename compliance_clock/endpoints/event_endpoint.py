import json
from flask import (
    Blueprint,
    request,
    jsonify,
    g
)
from ..models import Event

bp = Blueprint('event', __name__)

@bp.route('/event', methods=['PUT'])
def add_event():
    # assert request.data
    record = json.loads(request.data)
    event = Event(work_status=record['work_status'],
                  time=record['time'])
    if 'events' not in g:
        g.events = []
    g.events.append(event)
    
    return jsonify(event.to_json())
import json
from flask import (
    Blueprint,
    request,
    jsonify
)
from ..models import Event

bp = Blueprint('event', __name__)

@bp.route('/event', methods=['PUT', 'POST'])
def add_event():
    record = json.loads(request.data)
    event = Event(work_status=record['work_status'],
                  time=record['time'])
    event.save()
    return jsonify(event.to_json())
import json
from flask import (
    Blueprint,
    request,
    jsonify
)
from ..models import Event
from ..resources import events

bp = Blueprint('event', __name__)

# 
# `/event PUT` Add a new Event representing the end of a work state, a duration of Driving, Working, or Off Work
# * Parameters:
#   * `work_status : string` : One of `D` representing Driving, `W` representing Working, or `OFF` for Off Work
#   * `time : int` : number of minutes worker spent in work state
# * Return `json`: The created and persisted Event with the same fields as the parameters:
#   * `work_status : string` : One of `D` representing Driving,`W` representing Working, or `OFF` for Off Work
#   * `time : int` : number of minutes worker spent in work state

@bp.route('/event', methods=['PUT'])
def add_event():
    # assert request.data
    record = json.loads(request.data)
    event = Event(work_status=record['work_status'],
                  time=record['time'])
    events.save_event(event)
    return jsonify(event.to_json())
from ..models import Summary, Event

from flask import (
    Blueprint,
    jsonify
)

bp = Blueprint('summary', __name__)

@bp.route('/summary', methods=['GET'])
def get_summary():
    events = Event.objects()

    drive_clock = Summary('D', events)
    work_clock = Summary('W', events)

    return jsonify([drive_clock.to_json(),
                    work_clock.to_json()])

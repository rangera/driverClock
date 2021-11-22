from ..models import Clock

from flask import (
    Blueprint,
    jsonify,
    g
)

bp = Blueprint('clock', __name__)

@bp.route('/clock', methods=['GET'])
def get_clock():
    events = g.events if 'events' in g else []

    drive_clock = Clock('D', events)
    work_clock = Clock('W', events)

    return jsonify([drive_clock.to_json(),
                    work_clock.to_json()])

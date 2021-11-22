from ..models import Clock
from ..resources import events

from flask import (
    Blueprint,
    jsonify
)

bp = Blueprint('clock', __name__)

#
# `/clock GET` Get two clocks, built using previously submitted events. If time Off Work reaches `10` hours, clocks are reset. First is Drive clock, Second is Work clock
# * Parameters: None
# * Return `json`: Two Clocks with the following properties:
#   * `type : string` : One of `DRIVE_CLOCK` representing the Drive clock,`WORK_CLOCK` representing Work clock
#   * `violation_status : string` : Regulation status of the clock. One of `OK` if clock is within regulation,`V` if clock is in violation
#   * `time_value : int` : number of minutes worker has on this clock since last reset, for `DRIVE_CLOCK` only `D`-Driving time is counted, for `WORK_CLOCK` all three are summed(`D`, `W`-Non-driving Work, `OFF`-Time not worked [breaks less than 10 consecutive hours])

@bp.route('/clock', methods=['GET'])
def get_clock():
    all_events = events.get_all_events()
    drive_clock = Clock('D', all_events)
    work_clock = Clock('W', all_events)

    return jsonify([drive_clock.to_json(),
                    work_clock.to_json()])

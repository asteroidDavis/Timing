from chalice import Chalice

from timing import Timing

app = Chalice(app_name='timing')

# TODO: setup/import table connection objects


@app.route('/power/timing/{observation_name}', methods=['PUT'])
def post_observation(observation_name: str):
    request = app.current_request
    body = request.json_body
    try:
        Timing(sps=body['samplesPerSecond'], npts=body['numberOfPoints'], observation_name=observation_name)
    except KeyError:
         #TODO: missing parameters
        pass
    except Exception:
        # TODO: log unhandled error
        pass

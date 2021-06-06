from flask import Flask, request, jsonify, abort
import gpxpy
import gpxpy.gpx
from datetime import datetime

app = Flask(__name__, static_url_path='', static_folder='static')
app.config["DEBUG"] = True

tracks = {}

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')


@app.route('/api/v1/tracks', methods=['GET'])
def api_all():
    return jsonify([*tracks])


@app.route('/api/v1/gpx', methods=['GET'])
def api_gpx():
    name = request.args.get('name', 'default')
    if not name in tracks:
        abort(404)

    gpx = gpxpy.gpx.GPX()

    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for p in tracks[name]:
        gpx_segment.points.append(p)

    return gpx.to_xml()


@app.route('/api/v1/track', methods=['POST'])
def api_upload():
    time = datetime.fromtimestamp(int(request.form.get('time')))
    name = request.form.get('name', 'default') + '_' + time.strftime("%Y-%m-%d")
    if name not in tracks:
        tracks[name] = []

    tracks[name].append(gpxpy.gpx.GPXTrackPoint(
        latitude=request.form.get('lat'),
        longitude=request.form.get('lon'),
        elevation=request.form.get('alt'),
        time=time,
        speed=request.form.get('speed'),
        comment="battery:" + request.form.get('battery') + " gsm_signal:" + request.form.get('gsm_signal')
    ))
    return ''

app.run(host='0.0.0.0', port=5000) # todo hide behind reverse proxy

import flask
from flask import Flask, request, jsonify
import gpxpy
import gpxpy.gpx

app = Flask(__name__, static_url_path='', static_folder='static')
app.config["DEBUG"] = True

track = []

@app.route('/', methods=['GET'])
def home():
    return app.send_static_file('index.html')


@app.route('/api/v1/track', methods=['GET'])
def api_all():
    return jsonify(track)


@app.route('/api/v1/gpx', methods=['GET'])
def api_gpx():
    gpx = gpxpy.gpx.GPX()

    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)

    for p in track:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(p['lat'], p['lon'], elevation=p['alt']))

    return gpx.to_xml()


@app.route('/api/v1/track', methods=['POST'])
def api_upload():
    track.append(request.form)
    return ''

app.run(host='0.0.0.0')

# Locus Map Live Tracking

## Prepare
```bash
cd static
git clone https://github.com/mpetazzoni/leaflet-gpx
```

## Run it directly
```bash
pip3 install -r requirements.txt
python app.py
```

## Dockerized Execution
```bash
docker build -t livetracking:latest .
docker run --rm --publish 5000:5000 --name livetracking livetracking:latest
```

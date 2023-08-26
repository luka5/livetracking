# Locus Map Live Tracking

## Prepare
Clone this repo including the submodule.

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

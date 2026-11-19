# Docker

Containerization of the Flask API (`app/app.py`)

## Dockerfile (`app/Dockerfile`)

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

- `requirements.txt` is copied and installed before `app.py` so the dependency layer stays cached when the code changes
- `RUN` executes at build time, `CMD` executes when the container starts
- `EXPOSE` only documents the port, publishing it is done with `-p` at run time
- `.dockerignore` excludes `.venv/` and `__pycache__/` from the build context

## Build and run

```bash
cd app
docker build -t devops-api .
docker run -d -p 5000:5000 --name api devops-api
curl http://localhost:5000/
curl http://localhost:5000/disk
```

## Verified results

- Image `devops-api` is 197 MB (base `python:3.13-slim` is 178 MB)
- Build context sent to the daemon: 5.6 kB thanks to `.dockerignore`
- `docker ps` shows the container running `python app.py` with port `5000->5000`
- `/` returns `{"message":"DevOps Lab API","status":"ok"}`

## Disk usage inside the container

`/disk` uses `shutil.disk_usage("/")`, and inside the container `/` is an `overlay` filesystem backed by the host disk, so it reports the same size and usage as the VM (`df -h /`: 9.8G total, 4.6G used)

The percentage differs slightly because the formulas differ:

- API: `used / total` → 46.9 %
- `df`: `used / (used + available)` → 50 %

## Known limitations

- Flask development server in use, gunicorn not configured yet
- The VM runs Python 3.14 while the image uses 3.13
- Docker uses the legacy builder because `buildx` is not installed

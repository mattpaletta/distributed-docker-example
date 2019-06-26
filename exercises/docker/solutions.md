# Docker Example

### Basic Tasks
* run an instance of the `redis:latest` image on your machine
```bash
docker run redis:latest
```

* build and run a image/container for the code in ‘run_docker/` on Github

Dockerfile
```dockerfile
FROM python:3.7
ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
ADD main.py /main.py
ENTRYPOINT ["python3", "main.py"]
```

Docker command (run from within `run_docker` directory)
```bash
docker image build -t run_docker:latest .
```
FROM python:3.7

# Generate Protobuf
RUN pip3 install grpcio-tools grpcio
ADD weather.proto /weather.proto
RUN python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ weather.proto

# Install dependencies
ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

# Copy our app
ADD __init__.py /__init__.py
ADD main.py /main.py
ENTRYPOINT ["python3", "main.py"]
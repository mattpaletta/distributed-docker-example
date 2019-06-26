protos:
	python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ helloworld.proto

server: protos
	python3 main_server.py

client: protos
	python3 main_client.py
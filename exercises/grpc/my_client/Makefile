protos:
	python3 -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ --mypy_out=./ calc.proto

server: protos
	python3 main_server.py

client: protos
	python3 main_client.py
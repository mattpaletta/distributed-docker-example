import grpc

from helloworld_pb2 import HelloData, GoodbyeData
from helloworld_pb2_grpc import HellogRPCStub

if __name__ == "__main__":
    channel = grpc.insecure_channel('localhost:4620')
    hello_stub = HellogRPCStub(channel)

    hello_data = HelloData(x = 1, y = 2, user = "student")
    response: GoodbyeData = hello_stub.do_the_thing(request = hello_data)
    print("Received: " + str(response.the_thing))

from concurrent import futures
from time import sleep
import grpc

from helloworld_pb2 import HelloData, GoodbyeData
from helloworld_pb2_grpc import HellogRPCServicer, add_HellogRPCServicer_to_server

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HellogRPCServiceImpl(HellogRPCServicer):
    def do_the_thing(self, request: HelloData, context: grpc.RpcContext = None):
        x = request.x
        y = request.y
        user = request.user
        print("Got request from: ", user)
        return GoodbyeData(the_thing = x + y)


if __name__ == "__main__":
    hello_port = 4620
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    add_HellogRPCServicer_to_server(servicer = HellogRPCServiceImpl(), server = server)
    server.add_insecure_port('localhost:{0}'.format(hello_port))
    server.start()
    while True:
        sleep(ONE_DAY_IN_SECONDS)

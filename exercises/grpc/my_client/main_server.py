from concurrent import futures
from time import sleep
import grpc

from calc_pb2 import Number, Calculation
from calc_pb2_grpc import CalculatorServicer, add_CalculatorServicer_to_server

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CalculatorImplementation(CalculatorServicer):
    def get_add(self, request: Calculation, context: grpc.RpcContext = None) -> Number:
        x = request.x
        y = request.y
        return Number(n = x + y)

    def get_mult(self, request: Calculation, context: grpc.RpcContext = None) -> Number:
        x = request.x
        y = request.y
        return Number(n = x * y)


if __name__ == "__main__":
    calc_port = 1234
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    add_CalculatorServicer_to_server(servicer = CalculatorImplementation(), server = server)
    server.add_insecure_port('localhost:{0}'.format(calc_port))
    server.start()
    while True:
        sleep(ONE_DAY_IN_SECONDS)

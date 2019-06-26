from concurrent import futures
from time import sleep
import grpc
import redis
from weather import Weather, Unit

from weather_pb2 import WeatherCity, Location, CurrentWeather
from weather_pb2_grpc import WeatherServicer, add_WeatherServicer_to_server

ONE_DAY_IN_SECONDS = 60 * 60 * 24


class WeatherImplementation(WeatherServicer):
    def __init__(self):
        self._weather = Weather(unit = Unit.CELSIUS)
        self._redis_conn = redis.StrictRedis(host = "cache", port = 6379)

    def get_weather(self, request: WeatherCity, context: grpc.RpcContext = None):
        city = request.city
        cache_value = self._redis_conn.get(city)
        if cache_value is None:
            location = self._weather.lookup_by_location(city)
            condition = location.condition

            self._redis_conn.set(name = city, value = "|".join([condition.text,
                                                                str(condition.date),
                                                                condition.temp,
                                                                condition.temp]))

            return CurrentWeather(text = condition.text,
                                  date = str(condition.date),
                                  high = condition.temp,
                                  low = condition.temp)
        else:
            # We use the cached value
            text, date, high, low = cache_value.split("|")
            return CurrentWeather(text = text,
                                  date = date,
                                  high = high,
                                  low = low)

    def get_location(self, request: Location, context: grpc.RpcContext = None):
        lat = request.latitude
        long = request.longitude

        cache_value = self._redis_conn.get(str(lat) + "|" + str(long))
        if cache_value is None:
            location = self._weather.lookup_by_latlng(lat = lat, lng = long)
            condition = location.condition

            self._redis_conn.set(name = str(lat) + "|" + str(long), value = "|".join([condition.text,
                                                                                      str(condition.date),
                                                                                      condition.temp,
                                                                                      condition.temp]))

            return CurrentWeather(text = condition.text,
                                  date = str(condition.date),
                                  high = condition.temp,
                                  low = condition.temp)
        else:
            # We use the cached value
            text, date, high, low = cache_value.split("|")
            return CurrentWeather(text = text,
                                  date = date,
                                  high = high,
                                  low = low)


if __name__ == "__main__":
    hello_port = 4620
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    add_WeatherServicer_to_server(servicer = WeatherImplementation(), server = server)
    server.add_insecure_port('[::]:{0}'.format(hello_port))
    server.start()
    while True:
        sleep(ONE_DAY_IN_SECONDS)

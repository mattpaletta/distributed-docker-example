import grpc

from weather_pb2 import WeatherCity, Location, CurrentWeather
from weather_pb2_grpc import WeatherStub


if __name__ == "__main__":
    channel = grpc.insecure_channel('weather:4620')
    weather_stub = WeatherStub(channel)

    hello_city = WeatherCity(city = "victoria")
    response: CurrentWeather = weather_stub.get_weather(hello_city)
    print("City Forecast: " + str(response.text))

    hello_location = Location(latitude = 48.4634, longitude = 123.3117)
    response: CurrentWeather = weather_stub.get_location(hello_location)
    print("Location Forecast: " + str(response.text))

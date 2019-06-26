config:
	cp weather.proto weather/weather.proto
	cp weather.proto client/weather.proto

test config:
	docker-compose up --build &
	docker-compose wait client
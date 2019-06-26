import redis

if __name__ == "__main__":
    redis_conn = redis.StrictRedis(host = "bar", port = 6379)

    redis_conn.set(name = "cat", value = 1)
    redis_conn.set(name = "dog", value = 2)
    redis_conn.set(name = "mouse", value = 3)

    result = str(redis_conn.get(name = "cat"))
    print(result)

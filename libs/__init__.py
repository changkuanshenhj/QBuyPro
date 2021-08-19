from redis import Redis


config = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': '4',
    'decode_responses': True
}
rd_client = Redis(**config)


if __name__ == '__main__':
    rd_client.keys('*')
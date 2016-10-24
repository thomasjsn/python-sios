import configparser
import os
import redis

__Config = configparser.ConfigParser()
__Config.read(os.path.dirname(os.path.realpath(__file__)) + '/sios.conf')


def config(section, key):
    return __Config.get(section, key)


def redis_server():
    return redis.StrictRedis(
        host=__Config.get('redis', 'host'),
        port=__Config.get('redis', 'port'),
        db=__Config.get('redis', 'db')
    )

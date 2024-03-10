from urllib.parse import quote_plus

from pymongo import MongoClient

from licsber.env import get_env


def get_mongo(
        user=get_env('L_MONGO_USER'),
        pwd=get_env('L_MONGO_PWD'),
        host=get_env('L_MONGO_HOST'),
        port=get_env('L_MONGO_PORT'),
        connect=True,
) -> MongoClient:
    """
    获取Mongo数据库连接, 用于爬虫.
    :param user: 具有数据库权限的用户名.
    :param pwd: 密码.
    :param host: mongodb的url.
    :param port: host的端口.
    :param connect: 是否默认连接.
    :return: Mongo数据库连接.
    """

    user = quote_plus(user)
    pwd = quote_plus(pwd)

    conn_str = f"mongodb://{user}:{pwd}@{host}:{port}/main?retryWrites=true"
    client = MongoClient(
        conn_str,
        uuidRepresentation='standard',
        serverSelectionTimeoutMS=5000,
        connect=connect,
    )

    return client

import datetime
import time


def build_gmt_expired_time(expire_time):
    """生成GMT格式的请求超时时间
    :param int expire_time: 超时时间，单位秒
    :return str GMT格式的超时时间
    """
    now = int(time.time())
    expire_syncpoint = now + expire_time

    expire_gmt = datetime.datetime.fromtimestamp(expire_syncpoint).isoformat()
    expire_gmt += 'Z'

    return expire_gmt


expire_time = 300
build_gmt_expired_time(expire_time)

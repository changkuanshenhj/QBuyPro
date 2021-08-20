import time

from celery import shared_task
from libs import cache


@shared_task
def qbuy_task(user_id, goods_id):
    time.sleep(10)
    # 判断是否已抢完
    if cache.is_buyable():
        # 判断当前用户是否已抢过
        if not cache.exist_qbuy(user_id):
            cache.add_qbuy(user_id, goods_id)
        else:
            return ' %s 抢购 %s 失败:已抢过，限制一次' % (user_id, goods_id)

    return ' %s 抢购 %s 失败' % (user_id, goods_id)

# celery -A QBuyPro worker -P eventlet -l info

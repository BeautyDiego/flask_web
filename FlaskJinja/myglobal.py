import redis

global _global_pool

def _init():#初始化
    global _global_pool
    _global_pool = redis.ConnectionPool(host='192.168.2.114', port=6379,decode_responses=True,password='123456')



def get_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global _global_pool
    return _global_pool

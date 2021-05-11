import redis

# decode_responses 解析成字符串
# r = redis.Redis(host='39.105.171.7', port=6379, decode_responses=True)

pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set("food", "noodles", ex=3)
r.set("a", "ssss")
print(r['food'], type(r['food']))
print(r.get('a'), type(r.get('a')))
r.set('k1', 'v1')
r.set('k2', 'v2')
r.mset({'k1': "v4", 'k2': "v5"})
print(r['k1'])
print(r['k2'])
print(r.getset("k2", "v8"))
print(r['k2'])
print("======================================")
r.set("cn_name", "君惜大大")  # 汉字
print(r.getrange("cn_name", 0, 2))  # 取索引号是0-2 前3位的字节 君 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("cn_name", 0, -1))  # 取所有的字节 君惜大大 切片操作
r.set("en_name", "junxi")  # 字母
print(r.getrange("en_name", 0, 2))  # 取索引号是0-2 前3位的字节 jun 切片操作 （一个汉字3个字节 1个字母一个字节 每个字节8bit）
print(r.getrange("en_name", 0, -1))  # 取所有的字节 junxi 切片操作
print("======================================")
r.set("foo", "1")  # 0110001
r.set("foo1", "2")  # 0110010
print(r.mget("foo", "foo1"))  # ['goo1', 'baaanew']
print(r.bitop("AND", "new", "foo", "foo1"))  # "new" 0 0110000
print(r.mget("foo", "foo1", "new"))

source = "12"
for i in source:
    num = ord(i)
    print(num)  # 打印每个字母字符或者汉字字符对应的ascii码值 f-102-0b100111-01100111
    print(bin(num))  # 打印每个10进制ascii码值转换成二进制的值 0b1100110（0b表示二进制）
    print(bin(num).replace('b', ''))  # 将二进制0b1100110替换成01100110

print("======================================")

# r.hset("hash1", "k1", "v1")
# r.hset("hash1", "k2", "v2")
# print(r.hkeys('hash1'))
# print(r.hget('hash1', 'k1'))
# print(r.hmget('hash1', 'k1', 'k2'))
# r.hsetnx('hash1', 'k2', 'v3')
# print(r.hget('hash1', 'k2'))
#
# print("======================================")
# r.lpush("list1", 11, 22, 33)
# print(r.lrange('list1', 0, -1))
# r.rpush("list2", 11, 22, 33)
# print(r.llen('list2'))
# print(r.lrange('list2', 0, 3))
# print("======================================")
# print(r.lindex('list2', 0))
# r.rpoplpush('list1', 'list2')
# print(r.lrange('list1', 0, -1))
# print(r.lrange('list2', 0, -1))
r.sadd("set1", 1, 23, 4, 5, 88, 95, 35)
print(r.scard('set1'))
print(r.smembers('set1'))
# print(r.sscan('set1'))
# for i in r.sscan_iter("set1"):
#     print(i)
r.sadd("set2", 11, 23, 5, 22)
print(r.smembers('set2'))
print(r.sinter('set1', 'set2'))
print(r.sdiff('set1', 'set2'))
print(r.sdiff('set2', 'set1'))
r.sdiffstore('set3', 'set1', 'set2')
print(r.smembers('set3'))
print(r.sunion("set1", "set2"))  # 取2个集合的并集
print(r.sunionstore("set3", "set1", "set2"))  # 取2个集合的并集
print(r.smembers("set3"))
print(r.sismember('set1', 1))
print(r.sismember('set1', 2))
r.smove("set1", "set2", 4)
print(r.smembers("set1"))
print(r.smembers("set2"))

r.connection_pool.disconnect()

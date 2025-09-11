import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


r.set('foo', 'bar')
# True
out = r.get('foo')
# bar
print(out)

r.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})
# True

r.hgetall('user-session:123')
# {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}
print(r.hgetall('user-session:123'))
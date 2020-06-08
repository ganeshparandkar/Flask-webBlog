from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer('secret', 30) #after 30seconds it will give a error
token = s.dumps({'user_id': 1}).decode('utf-8')
print(token)

a = s.loads(token)
print(a)

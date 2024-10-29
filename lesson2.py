list1 = [1, 2, 3, 'привет!']

list2 = [1, 1, 2, 2, 3, 4]
# print(list2)

list2 = list(set(list2))
# print(list2)


# print(list1)

d1 = dict()
# print(d1)

d1["first"] = 1
d1["second"] = 12345

d1["first"] = 'hello!'

# print(d1)

# print(d1.get("second"))
# print(d1["second"])

# d2 = dict()
d2 = {
    "val1": 1,
    "val2": 'hello123',
    1: 'test'
}

# print(d2)
# print(d2.get(1))

# print(d2.keys())
# print(d2.values())
# print(type(d2.values()))

d3 = dict()
d3['new'] = d2
d3['old'] = None
# print(d3)

# print(d3.get('new').get(1))

l4 = [d3, d2]
# print(l4)

l5 = list(d3.keys())
# print(l5)

a = (1, 2, 3) #тайпл
# print(a)
# print(a[2])

# print(d2.items())

ll1 = [1, 2, 3, 4]
ll2 = ['a', 'b', 'c']
# print(ll1+ll2)


# s3 = """lfkjglkghjflghjflgkhj
# fghfghfghfgh
# fghfghfg
# """
# print(s3)

# if l5:
#     print('hello')
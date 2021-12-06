import bench

def test(num):
    for _ in iter(range(num//10000)):
        l = [0] * 1000
        l2 = list(map(lambda x: x, l))

bench.run(test)

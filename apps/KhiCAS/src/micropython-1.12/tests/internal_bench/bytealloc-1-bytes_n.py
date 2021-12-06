import bench

def test(num):
    for _ in iter(range(num // 1000)):
        bytes(10000)

bench.run(test)

import bench

def test(num):
    for _ in iter(range(num//20)):
        enumerate([1, 2], 1)

bench.run(test)

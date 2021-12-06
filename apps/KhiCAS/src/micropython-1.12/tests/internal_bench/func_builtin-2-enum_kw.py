import bench

def test(num):
    for _ in iter(range(num//20)):
        enumerate(iterable=[1, 2], start=1)

bench.run(test)

import bench

def test(num):
    for _ in iter(range(num // 1000)):
        b"\0" * 10000

bench.run(test)

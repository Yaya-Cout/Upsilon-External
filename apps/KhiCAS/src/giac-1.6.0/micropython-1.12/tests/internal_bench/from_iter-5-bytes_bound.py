import bench

def test(num):
    l = [0] * 1000
    l2 = bytes(l)

bench.run(test)

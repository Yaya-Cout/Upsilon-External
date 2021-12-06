import bench

def test(num):
    l = [0] * 1000
    l2 = bytearray(l)

bench.run(test)

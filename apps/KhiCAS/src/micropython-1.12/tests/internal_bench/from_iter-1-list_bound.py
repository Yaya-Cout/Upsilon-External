import bench

def test(num):
    l = [0] * 1000
    l2 = list(l)

bench.run(test)

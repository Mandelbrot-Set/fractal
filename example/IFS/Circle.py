from fractal import IFS
from fractal.ifs import getIfsCode
ifscode = [
    [0.27, 0.27, 0, 0, 1, 0, 1 / 9],
    [0.27, 0.27, 0, 0, 0.707, 0.707, 1 / 9],
    [0.27, 0.27, 0, 0, 0, 1, 1 / 9],
    [0.27, 0.27, 0, 0, -0.707, 0.707, 1 / 9],
    [0.27, 0.27, 0, 0, -1, 0, 1 / 9],
    [0.27, 0.27, 0, 0, -0.707, -0.707, 1 / 9],
    [0.27, 0.27, 0, 0, 0, -1, 1 / 9],
    [0.27, 0.27, 0, 0, 0.707, -0.707, 1 / 9],
    [0.5, 0.5, 22.5, 22.5, 0, 0, 1 / 9],
]
ifs = IFS([500, 500])
# ifs.setCoordinate()
ifs.setPx(100, 250, 250)
ifs.setIfsCode(getIfsCode(ifscode))
ifs.doIFS(200000)
ifs.wait()
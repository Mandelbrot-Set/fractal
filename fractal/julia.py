"""
Julia集
"""

import pygame
from .base import Base
from .colors import *
from threading import Thread


class Julia(Base):

    def __init__(self, size, title=""):
        Base.__init__(self, size, self.__run, title)
        self.setExp(2)
        self.setC(None)
        self.setRadius(2)
        self.width = size[0]
        self.height = size[1]
        self.setRange(3.5, 3.5)
        self.setCentre(0 + 0j)

    def setRadius(self, R):
        # 设置逃逸半径
        self.R = R

    def setC(self, C):
        # 设置参考值C
        self.C = C

    def setExp(self, expc):
        # 设置指数，默认2
        self.expc = expc

    def color(self, i, r=2):
        # 对第i次迭代点着色，返回RGB值
        if i < len(reds) - 1:
            return reds[i]
        return (0, 0, 0)

    def setColor(self, call):
        self.color = call

    def setCentre(self, z0):
        # 设置中心点
        self.z0 = z0

    def setRange(self, xmax, ymax):
        # 设置坐标范围，范围越小图放大倍数越高
        self.xmax = xmax
        self.ymax = ymax

    def __getXY(self, i, j):
        # 通过像素坐标获取映射后的坐标
        return complex((i / self.width - 0.5) * self.xmax + self.z0.real, (j / self.height - 0.5) * self.ymax + self.z0.imag)

    def scala(self, i, j, rate):
        # 将(i, j)像素点置于中心位置，放大rete倍
        self.setCentre(self.__getXY(i, j))
        self.xmax /= rate
        self.ymax /= rate

    def __calc(self, start, w, h):
        # 绘制以start为起点，宽w,高h的子区域
        # x,y,w,h,N,c
        for i in range(w):
            for j in range(h):
                ct = 0
                z = self.__getXY(start[0] + i, start[1] + j)
                for k in range(self.N):
                    ct = k
                    if abs(z) > self.R:  # 大于逃逸半径，则返回
                        break
                    z = z**self.expc + self.C
                self.screen.set_at(
                    [start[0] + i, start[1] + j], self.color(ct))

    def __run(self):
        # 线程中
        print("x range ：[-%f,%f]\ny range ：[-%f,%f]" % (
            self.xmax, self.xmax, self.ymax, self.ymax))
        if self.C == None:
            raise Exception("请设置迭代常数")
            return
        tn = 5  # 25 个子线程绘图
        ci = self.width // tn
        cj = self.height // tn
        ts = []
        for i in range(tn):
            for j in range(tn):
                t = Thread(target=self.__calc, args=(
                    [i * ci, j * cj], self.width // tn, self.height // tn))
                t.start()
                ts.append(t)
        for t in ts:
            t.join()
        del ts

    def doJulia(self, N):
        # 进入迭代
        # N: 单点最大迭代次数
        self.N = N

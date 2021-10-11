
import sys
import json
import os
import numpy as np
import time

"""
参考链接：https://blog.csdn.net/a1103688841/article/details/89711120
NMS 检测框存储的是(x0, y0, x1, y1, score)
计算当前框面积，交集面积
交集 / (当前框 + 配对框 - 交集)
比例小于阈值的，合并到
"""
def py_cpu_nms(dets, thresh):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    scores = dets[:, 4]
    index = scores.argsort()[::-1]
    keep = []
    
    while index.size > 0:
        i = index[0]
        keep.append(i)
        x11 = np.maximum(x1[i], x1[index[1:]])
        y11 = np.maximum(y1[i], y1[index[1:]])
        x22 = np.minimum(x2[i], x2[index[1:]])
        y22 = np.minimum(y2[i], y2[index[1:]])

        w = np.maximum(0, x22 - x11 + 1)
        h = np.maximum(0, y22 - y11 + 1)

        overlap = w * h
        ious = overlap / (areas[i] + areas[index[1:]] - overlap)

        idx = np.where(ious <= thresh)[0]
        index = index[idx+1] # because index start from 1 

    return keep

if __name__ == '__main__':
    thresh = 0.7
    boxes=np.array([[100,100,210,210,0.72],
        [250,250,420,420,0.8],
        [220,220,320,330,0.92],
        [100,100,210,210,0.72],
        [230,240,325,330,0.81],
        [220,230,315,340,0.9]])
    
    out = py_cpu_nms(boxes, thresh)
    
    print(out)#[2, 1, 3]

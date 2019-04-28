"""
    design by momo
"""

import cv2
import numpy as np
from os import walk
from os.path import join
import os,shutil

def cropImg(frame):
    sp = frame.shape  # obtain the image shape
    sz1 = sp[0]  # height(rows) of image
    sz2 = sp[1]  # width(colums) of image
    a = int(sz1 / 2 - 75)  # x start
    b = int(sz1 / 2 + 75)  # x end
    c = int(sz2 / 2 - 75)  # y start
    d = int(sz2 / 2 + 75)  # y end
    cropImg = frame[a-25:b-25, c-100:d-100]
    return cropImg

def create_descriptors(folder):
    files = []
    for (dirpath, dirnames, filenames) in walk(folder):
        files.extend(filenames)
    for f in files:
        if '.jpg' in f:
            save_descriptor(folder, f, cv2.xfeatures2d.SIFT_create())

def save_descriptor(folder, image_path, feature_detector):
    # 判断图片是否为npy格式
    if image_path.endswith("npy"):
        return
    # 读取图片并检查特征
    img = cv2.imread(join(folder,image_path), 0)
    keypoints, descriptors = feature_detector.detectAndCompute(img, None)
    # 设置文件名并将特征数据保存到npy文件
    descriptor_file = image_path.replace("jpg", "npy")
    np.save(join(folder, descriptor_file), descriptors)

def match(folder, image_path):
    query = cv2.imread(image_path, 0)
    descriptors = []
    # 获取特征数据文件名
    for (dirpath, dirnames, filenames) in walk(folder):
        for f in filenames:
            if f.endswith("npy"):
                descriptors.append(f)
        # print(descriptors)

    # 使用SIFT算法检查图像的关键点和描述符
    sift = cv2.xfeatures2d.SIFT_create()
    query_kp, query_ds = sift.detectAndCompute(query, None)

    # 创建FLANN匹配器
    index_params = dict(algorithm=0, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    potential_culprits = {}
    for d in descriptors:
        # 将图像query与特征数据文件的数据进行匹配
        matches = flann.knnMatch(query_ds, np.load(join(folder, d)), k=2)
        # 清除错误匹配
        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)
        # 输出每张图片与目标图片的匹配数目
        # print("img is %s ! matching rate is (%d)" % (d, len(good)))
        potential_culprits[d] = len(good)

    # 获取最多匹配数目的图片
    max_matches = None
    sum_matches=0
    potential_suspect = None
    for culprit, matches in potential_culprits.items():
        sum_matches+=matches
        if max_matches == None or matches > max_matches:
            max_matches = matches
            potential_suspect = culprit
    mean_matches =sum_matches/potential_culprits.__len__()
    print("potential suspect is %s,matching rate is %d" % (potential_suspect.replace("npy", "").upper(),max_matches))
    print("mean matching rate is %f" % mean_matches)
    # if max_matches < 5:
    #     cv2.imwrite(str(descriptors.__len__()+5)+'.jpg', query)
    return (max_matches,mean_matches,str(potential_suspect.replace("npy", "").upper()))

def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy %s -> %s"%( srcfile,dstfile))

def append(folder, image_path):
    i=0
    for (dirpath, dirshutiles, filenames) in walk(folder):
        for f in filenames:
            if f.endswith("jpg"):
                i+=1
    mycopyfile(image_path,folder+'/'+str(i+1)+'.jpg')
    return str(i+1)+'.jpg'


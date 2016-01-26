#encoding:UTF-8
import os
import numpy as np
from pysqlite2 import dbapi2 as sqlite
import cv2


class Indexer(object):
    def __init__(self, db):
        """初始化数据库的名称及词汇对象"""
        self.con = sqlite.connect(db)

    def __del__(self):
        self.con.close()

    def db_commit(self):
        self.con.commit()

    def create_tables(self):
        """创建数据库表单"""
        self.con.execute('create table images(imid INTEGER PRIMARY KEY autoincrement, location, a_year, a_month, a_day, a_rgb, a_hour, a_min, a_sec, a_type, a_file BLOB, a_rfile BLOB)')
        self.db_commit()

    def insert_data(self, count, names, type, g, rg):
        sql = 'insert into images(imid, location, a_year, a_month, a_day, a_rgb, a_hour, a_min, a_sec, a_type, a_file, a_rfile) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        self.con.execute(sql, (count, names[0], names[1], names[2], names[3], names[4], names[5], names[6], names[7], type, g, rg))


def parse_filename(file_name):
    # N20031221G041301
    filename_list = []
    filename_list.append(file_name[0])
    filename_list.append(file_name[1:5])
    filename_list.append(file_name[5:7])
    filename_list.append(file_name[7:9])
    filename_list.append(file_name[9])
    filename_list.append(file_name[10:12])
    filename_list.append(file_name[12:14])
    filename_list.append(file_name[14:])
    return filename_list


def img_data(file):
    file = cv2.imread(file)
    _, g, _ = cv2.split(file)
    rg = cv2.resize(g, (256, 256))
    # cv2.imshow('test', file)
    # cv2.imshow('rgsize', rg)
    # cv2.waitKey(0)
    g = g.reshape((1, -1))
    rg = rg.reshape((1, -1))
    return g, rg


if __name__=='__main__':
    url = '/home/aurora/hdd/workspace/PycharmProjects/data/aurora2/'
    save_path = '/home/aurora/hdd/workspace/PycharmProjects/data/aurora2'
    # db = Indexer('/home/aurora/hdd/workspace/PycharmProjects/data/aurora2/all.db')
    # db.create_tables()
    IMAGE_SIZE = 256*256
    for i in ['1', '2', '3', '4']:
        dir = url+i
        temp = save_path+'/type'+i
        index = 0
        count = len(os.listdir(dir))
        data = np.zeros((count, IMAGE_SIZE+1))
        for f in os.listdir(dir):
            path = os.path.join(dir, f)
            g, rg = img_data(path)
            data[index, 0] = int(i)
            data[index, 1:] = rg
        print data
        print data.shape
        np.save(temp, data)


# coding:utf-8
import requests
from hashlib import md5
import os
from selenium import webdriver
import time
from PIL import Image

class RClient(object):

    def __init__(self, username, password, soft_id, soft_key):
        password='ztc731985'
        self.username = 'ztc950821'
        self.password = md5(password.encode('utf-8')).hexdigest()
        self.soft_id = '99886'
        self.soft_key = '4d3cc75c3cb44a91bcbdd736300c38ff'
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': (r'C:\Users\93181\Desktop\parttimejob\login\checkcode.png', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


def open_webpage():
    drive=webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    drive.get(r'https://passport.aicai.com/xpassport/aicai/login/index?redirectUrl=https://kaijiang.aicai.com/cqssc/')
    drive.maximize_window()
    drive.save_screenshot(r'C:\Users\93181\Desktop\parttimejob\login\screenshot.png')
    imgelement = drive.find_element_by_id('RIC')
    location = imgelement.location
    size = imgelement.size
    rangle = (1455,392,1477+size['width'],395+size['height'])
    i = Image.open(r"C:\Users\93181\Desktop\parttimejob\login\screenshot.png")
    bb = i.crop(rangle)
    bb.save(r"C:\Users\93181\Desktop\parttimejob\login\checkcode.png","PNG")
    rc = RClient('username', 'password', 'soft_id', 'soft_key')
    im = open(r'C:\Users\93181\Desktop\parttimejob\login\checkcode.png', 'rb').read()
    data=str(rc.rk_create(im, 3040))
    print(data[12:16])

open_webpage()


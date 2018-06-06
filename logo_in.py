# coding:UTF-8
import os
from selenium import webdriver
import time
from PIL import Image
import pytesseract
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
#cc = Image.open(r"C:\Users\93181\Desktop\parttimejob\login\checkcode.jpg")
text = pytesseract.image_to_string(r"C:\Users\93181\Desktop\parttimejob\login\checkcode.png").strip()
user = drive.find_element_by_id("accountLogin")
user.send_keys("18020622687")
password = drive.find_element_by_id("passwordLogin")
password.send_keys("ZTCSHIDOG")
checkcode = drive.find_element_by_id("checkCode")
check.send_keys(text)
drive.find_element_by_id("loginPgBtn").click()

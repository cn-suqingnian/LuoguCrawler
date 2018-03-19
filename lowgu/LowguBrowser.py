"""
简单的爬虫项目来访问洛谷官网
"""
from http import cookiejar
from urllib import parse, request
from bs4 import BeautifulStoneSoup
import json
import socket
import gzip


__author__ = "Himself65"
__license__ = "MIT"

class LowguBrowser:
    _headers = {}

    def __init__(self):
        """
        初始化访问洛谷
        """
        self._headers[
            'user-agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        self._headers['accept-encoding'] = "gzip, deflate, br"
        self._headers['accept-language'] = "zh,en;q=0.9,zh-CN;q=0.8,ja;q=0.7"
        self.setOpener()

    # def __str__(self):
    #     # TODO

    def insert_headers(self, key, value):
        self._headers[key] = value
        self.setOpener()

    def setOpener(self):
        cj = cookiejar.CookieJar()
        pro = request.HTTPCookieProcessor(cj)
        self.opener = request.build_opener(pro)
        header = []
        for key, value in self._headers.items():
            elem = (key, value)
            header.append(elem)
        self.opener.add_handler = header

    def openURL(self, url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.response = self.opener.open(url, data=data, timeout=timeout)

    def getData(self):
        data = self.response.read()

        return data.decode()

    @staticmethod
    def create_query_string_message(dictionary):
        """ create_query_string_message(dictionary) -> String
            dictionary -> 字典，例如：
            { 
                "id": 761282619,
                "name": "himself65" 
            }
            将返回 "id=761282619&name=himself65"
        """
        s = ""
        for (key, value) in dictionary:
            s = s + key + "=" + value + "&"
        return s.rstrip("&")

    @staticmethod
    def getDataFromResponse(response, data):
        messages = json.loads(response)
        return messages[data]

    @staticmethod
    def check_Accessible(data):
        """
            
        """
        data_json = json.loads(data)
        return data['status'] == 200 if True else False
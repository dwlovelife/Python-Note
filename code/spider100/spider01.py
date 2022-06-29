"""
爬取锋鸟网
"""

import requests
import json

class Spider():

    def __init__(self):
        self._requestHeader = {
            'Host': 'photo.fengniao.com',
            'Referer': ''
        }


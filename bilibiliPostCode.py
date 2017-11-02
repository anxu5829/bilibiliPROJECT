import pandas as pd
import numpy as np

import requests

import requests, re, os, traceback



data = {'mid'	:'123484','csrf':'05b417fdfcf160becb70dc0a67e740fd'}
headers = {'Host':'space.bilibili.com',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',

'Content-Type':'application/x-www-form-urlencoded',
'X-Requested-With':'XMLHttpRequest',
'Referer':'http://space.bilibili.com/123484/',

 }
r = requests.post('https://space.bilibili.com/ajax/member/GetInfo',headers=headers,data=data).json()

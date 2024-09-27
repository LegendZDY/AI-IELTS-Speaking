import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import wave
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import os

import dashscope
from dashscope.audio.tts_v2 import *

try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError(
        'Python environment for SPARK AI is not completely set up: required package "python-dotenv" is missing.') from None

from pathlib import Path
env_path = Path('./config') / '.env'
# print(env_path)
load_dotenv(dotenv_path=env_path)


STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识



class tts_Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, Text):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.Text = Text

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.BusinessArgs = {"aue": "raw", "auf": "audio/L16;rate=16000", "vcn": "xiaoyan", "tte": "utf8"}
        self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-8')), "UTF8")}
        #使用小语种须使用以下方式，此处的unicode指的是 utf16小端的编码方式，即"UTF-16LE"”
        #self.Data = {"status": 2, "text": str(base64.b64encode(self.Text.encode('utf-16')), "UTF8")}

    # 生成url
    def create_url(self):
        url = 'wss://tts-api.xfyun.cn/v2/tts'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/tts " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        # print("date: ",date)
        # print("v: ",v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        return url

def tts_on_message(ws, message):
    try:
        message =json.loads(message)
        code = message["code"]
        sid = message["sid"]
        audio = message["data"]["audio"]
        audio = base64.b64decode(audio)
        status = message["data"]["status"]
        
        if code != 0:
            errMsg = message["message"]
            print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
        else:
            with open('./data/demo.pcm', 'ab') as f:
                f.write(audio)
        if status == 2:
            received_flag.append("sucess")
            print("ws is closed")
            ws.close()
        

    except Exception as e:
        print("receive msg,but parse exception:", e)

# 收到websocket错误的处理
def tts_on_error(ws, error):
    print("### error:", error)


# 收到websocket关闭的处理
def tts_on_close(ws,a,b):
    print("### closed ###")


# 收到websocket连接建立的处理
def tts_on_open(ws):
    def run(*args):
        d = {"common": CommonArgs,
             "business": BusinessArgs,
             "data": Data,
             }
        d = json.dumps(d)
        print("------>开始发送文本数据")
        ws.send(d)
        if os.path.exists('./data/demo.pcm'):
            os.remove('./data/demo.pcm')
    thread.start_new_thread(run, ())


def tts_wav_get(text_message, wav_file_name):
    global CommonArgs 
    global BusinessArgs 
    global Data
    global received_flag
    received_flag = []
    CommonArgs = {"app_id": os.getenv("APPID")}
    BusinessArgs = {"aue": "raw", "auf": "audio/L16;rate=16000", "vcn": "xiaoyan", "tte": "utf8"}
    Data = {"status": 2, "text": str(base64.b64encode(text_message.encode('utf-8')), "UTF8")}
    wsParam = tts_Ws_Param(APPID=os.getenv("APPID"), APISecret=os.getenv("APISecret"),
                    APIKey=os.getenv("APIKey"),
                    Text=text_message)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=tts_on_message, on_error=tts_on_error, on_close=tts_on_close)
    ws.on_open=tts_on_open
    

    def pcm_to_wav(pcm_file_path, wav_file_path, channels=1, sample_width=2, sample_rate=44100):
        """
        将 PCM 文件转换为 WAV 文件
        :param pcm_file_path: 输入的 PCM 文件路径
        :param wav_file_path: 输出的 WAV 文件路径
        :param channels: 声道数，1 为单声道，2 为立体声
        :param sample_width: 每个样本的字节数，2 表示 16 位（通常是 PCM 文件的格式）
        :param sample_rate: 采样率，通常为 44100 或 16000 等
        """
        with open(pcm_file_path, 'rb') as pcm_file:
            pcm_data = pcm_file.read()

        # 创建一个 WAV 文件
        with wave.open(wav_file_path, 'wb') as wav_file:
            # 设置 WAV 文件的参数
            wav_file.setnchannels(channels)        # 设置声道数
            wav_file.setsampwidth(sample_width)    # 设置样本宽度
            wav_file.setframerate(sample_rate)     # 设置采样率

            # 将 PCM 数据写入 WAV 文件
            wav_file.writeframes(pcm_data)
    
    def run2():
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    thread.start_new_thread(run2, ())
    while True:
        if received_flag:
            pcm_file = './data/demo.pcm'  # 替换为你的 PCM 文件路径
            wav_file = './data/'+ wav_file_name # 替换为你想要保存的 WAV 文件路径
            pcm_to_wav(pcm_file, wav_file, channels=1, sample_width=2, sample_rate=16000)
            break

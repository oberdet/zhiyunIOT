# python 3.9.2
import pymysql
import random
import time
import requests
import re
import json
from paho.mqtt import client as mqtt_client
from flask import Flask
from flask import request
import json
from flask import Flask, render_template, Response
import cv2
 
def gen_frames():
    camera = cv2.VideoCapture('rtmp://121.5.160.114:1935/stream/sbss')

    while True:
        # 一帧帧循环读取摄像头的数据
        success, frame = camera.read()
        if not success:
            break
        else:
            # 取值范围：0~100，数值越小，压缩比越高，图片质量损失越严重
            params = [cv2.IMWRITE_JPEG_QUALITY, 4]  # ratio:0~100
            # 将每一帧的数据进行编码压缩，存放在memory中
            ret, buffer = cv2.imencode('.jpg', frame,params)
            frame = buffer.tobytes()
            # 使用yield语句，将帧数据作为响应体返回，content-type为image/jpeg
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
 
def myjj():#名言警句API
    """名言警句API"""
    ur="https://hanyu.baidu.com/hanyu/api/sentencelistv2?query=%E5%90%8D%E4%BA%BA%E5%90%8D%E8%A8%80&src_id=51328&query_type=exact&type=sentence&pn=2&ps=20&smpid=&sentence_type=&tab_type=&gssda_res={%22sentence_type%22:%22%E5%90%8D%E8%A8%80%22}"
    a=requests.get(url=ur).text
    data=json.loads(a)
    literature_author=data["data"]["recommend"][0]["literature_author"]
    body=data["data"]["recommend"][0]["body"][0]
    article_info = {}
    data = json.loads(json.dumps(article_info))
    data['literature_author'] = literature_author
    data['body'] = body
    article = json.dumps(data, ensure_ascii=False)
    print(article)
    return article
class viewmysql():
    def __init__(self,master):
        self.host='ip'
        self.user="数据库用户名"
        self.passwd="数据库密码"

     
    def additme(self,clientid,topic,name):#添加设备
    # """向数据库添加设备"""
        conn =pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database="wlw")
        a=random.randint(1000, 9999)
        cs1 = conn.cursor()
        query = "INSERT INTO `itme` (`id`, `clientid`, `topic`, `ip`, `name`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(a,clientid,topic,ip,name)
        cs1.execute(query)
        conn.commit()
        cs1.close()
        conn.close()
    def daaview(self,view,gn,viewid):
    # """向数据库添加安卓view"""
        conn =pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database="wlw")
        a=random.randint(1000, 9999)
        cs1 = conn.cursor()
        query = "INSERT INTO `view` (`view`, `gn`, `viewid`, `id`) VALUES ('{}', '{}', '{}', '{}')".format(view,gn,viewid,a)
        cs1.execute(query)
        conn.commit()
        cs1.close()
        conn.close()
    def cxitme(self):
    # """查询数据库项目"""
        sql=pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database="wlw")
        cursor = sql.cursor(pymysql.cursors.DictCursor)
        sqlitm = '''SELECT * from itme'''
        cursor.execute(sqlitm)
        a = cursor.fetchall()
        cursor.close()
        sql.close()
        return a
    def cxview(self,viewid):
    # """查询数据库view"""
        sql=pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database="wlw")
        cursor = sql.cursor(pymysql.cursors.DictCursor)
        sqlitm = '''SELECT * from view where view.viewid={}'''.format(viewid)
        cursor.execute(sqlitm)
        a = cursor.fetchall()
        cursor.close()
        sql.close()
        return a
def publi(topic,msg):
    """mqtt消息发送"""
    broker = 'ip'
    port = 1883
    client_id = f'znwllw{random.randint(0, 1000)}'
    username = '222'
    password = '22'
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.connect(broker, port)
    client.publish(topic, msg)
def login():
    """登录消息服务器"""
    url="http://ip:18083/api/v5/login"
    data='{"username":"用户名","password":"密码"}'
    head={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'Bearer undefined',
    'Connection': 'keep-alive',
    'Content-Length': '46',
    'Content-Type': 'application/json',
    'Host':'ip:18083',
    'Origin': 'http://ip:18083',
    'Referer': 'http://ip:18083/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
    y=requests.session()
    a=y.post(url=url,data=data,headers=head).text
    datas=json.loads(a)
    print(datas["token"])
    had={'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Authorization': 'Bearer {}'.format(datas["token"]),
'Connection': 'keep-alive',
'Host': 'ip:18083',
'Referer': 'http://ip:18083/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
    url="http://ip:18083/api/v5/subscriptions?limit=500&page=1"
    b=y.get(url=url,headers=had).text
    da=json.loads(b)
    article_info = {}
    data = json.loads(json.dumps(article_info))
    ipaddr=""
    for i in range(len(da["data"])):
        
        data['sbmc{}'.format(i)] = '{}'.format(da["data"][i]["clientid"])
        data['sbzt{}'.format(i)] = '{}'.format(da["data"][i]["topic"])
        u="http://ip:18083/api/v5/clients/{}".format(da["data"][i]["clientid"])
        h={'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Authorization': 'Bearer {}'.format(datas["token"]),
'Connection': 'keep-alive',
'Host': 'ip:18083',
'Referer': 'http://ip:18083/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'
}
        ipa=y.get(url=u,headers=h).text
        ipaddr=json.loads(ipa)
        data['ip{}'.format(i)] = '{}'.format(ipaddr["ip_address"])
        print(da["data"][i]["clientid"])
        print(da["data"][i]["topic"])
    data["itme"]="{}".format(len(da["data"]))
    article = json.dumps(data, ensure_ascii=False)
    return article
app = Flask(__name__)
sqql=viewmysql()
# 根路由
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        publi(da["zhuti"],da["XX"])
        return '%s'% user_agent,200,[("token", "123456"), ("Set-Cookie", "shenzhen")]
    if request.method=="GET":
        user_agent = request.get_data()
        return '%s'% user_agent,200,[("token", "123456"), ("Set-Cookie", "shenzhen")]
@app.route('/zt',methods=['POST','GET'])
def abc():
    if request.method=="GET":
        a=login()
        return a
@app.route('/rgb',methods=['POST','GET'])
def rgb():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        publi(da["zhuti"],da["R"]+","+da["G"]+","+da["B"])
        print(da)
        return user_agent
# @app.route('/cp',methods=['POST','GET'])
# def cp():
#     if request.method=="POST":
#         user_agent ='{"name":"Arduino on ESP32","toolchainPrefix":"xtensa-esp32-elf","svdFile":"esp32.svd","request":"attach","postAttachCommands":["set remote hardware-watchpoint-limit 2","monitor reset halt","monitor gdb_sync","thb setup","c"],"overrideRestartCommands":["monitor reset halt","monitor gdb_sync","thb setup","c"]}'
#         return user_agent
#     if request.method=="GET":
#         user_agent ='{"name":"Arduino on ESP32","toolchainPrefix":"xtensa-esp32-elf","svdFile":"esp32.svd","request":"attach","postAttachCommands":["set remote hardware-watchpoint-limit 2","monitor reset halt","monitor gdb_sync","thb setup","c"],"overrideRestartCommands":["monitor reset halt","monitor gdb_sync","thb setup","c"]}'
#         return user_agent
@app.route('/dn',methods=['POST','GET'])
def dn():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        publi(da["zhuti"],da["zl"])
        return str(da["zhuti"])+str(da["zl"]),200
    if request.method=="GET":
        user_agent = request.get_data() 
        return user_agent
@app.route('/additme',methods=['POST','GET'])
def add():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        sqql.additme(da["clientid"],da["topic"],da["name"])
        return "yes",200
    if request.method=="GET":
        ssqql=sqql.cxitme()
        article_info = {}
        data = json.loads(json.dumps(article_info))
        for i in range(len(ssqql)):
            data["data{}".format(i)] = '{}'.format(ssqql[i])
        data["itme"]="{}".format(len(ssqql))
        article = json.dumps(data, ensure_ascii=False)
        user_agent = request.get_data() 
        return article,200
@app.route('/addview',methods=['POST','GET'])
def addview():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        sqql.daaview(da["view"],da["gn"],da["viewid"])
        return "yes",200
@app.route('/cxview',methods=['POST','GET'])
def cxviewww():
    if request.method=="POST":
        user_agent = request.get_data()
        da=json.loads(user_agent)
        ssqql=sqql.cxview(da["viewid"])
        article_info = {}
        data = json.loads(json.dumps(article_info))
        for i in range(len(ssqql)):
            data["data{}".format(i)] = '{}'.format(ssqql[i])
        data["itme"]="{}".format(len(ssqql))
        article = json.dumps(data, ensure_ascii=False)
        user_agent = request.get_data() 
        return article,200
@app.route('/myjjjj',methods=['POST','GET'])
def myjjj():
    if request.method=="GET":
        article=myjj()
        return article,200
@app.route('/vieod')
def video_start():
    # 通过将一帧帧的图像返回，就达到了看视频的目的。multipart/x-mixed-replace是单次的http请求-响应模式，如果网络中断，会导致视频流异常终止，必须重新连接才能恢复
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run('0.0.0.0',8999)

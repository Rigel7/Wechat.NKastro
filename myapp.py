# -*- coding: utf-8 -*-
import time
from flask import Flask,g,request,make_response
from selectreply import selrep
import hashlib
import xml.etree.ElementTree as ET
app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"] )
def wechat_auth():
    if request.method == "GET":
        token = "XFzGbfDrNsjt2hKr3Ek5"
        query = request.args
        signature = query.get("signature", "")
        timestamp = query.get("timestamp", "")
        nonce = query.get("nonce", "")
        echostr = query.get("echostr", "")
        s = [timestamp, nonce, token]
        s.sort()
        s = "".join(s)
        if ( hashlib.sha1(s).hexdigest() == signature ):
            return make_response(echostr)
    elif request.method == "POST":
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find("ToUserName").text
        fromu = xml_rec.find("FromUserName").text
        if xml_rec.find("MsgType").text=="event":
            if xml_rec.find("Event").text=="subscribe":
                content = "吾牵友肠人情暖，心系宇宙天地宽，欢迎来到南开天协～你愿意与小南南一起道穹宇、术科学、气自由吗？（回复“我愿意”开启奇妙星空之旅）"
                response = make_response("<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),content))
                response.content_type="application/xml"
                return response
        elif xml_rec.find("MsgType").text=="text":
            content = xml_rec.find("Content").text
            response = make_response(selrep(fromu,tou,content))
            response.content_type="application/xml"
            return response

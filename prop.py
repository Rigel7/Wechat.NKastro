# -*- coding: utf-8 -*-
import time,re,urllib2,json,base64,urllib,hashlib,hmac,datetime,sys
def apod(fromu,tou):
    netpage = urllib2.urlopen(r'http://www.phys.ncku.edu.tw/~astrolab/mirrors/apod/apod.html').read().decode('big5')
    picstart = netpage.find('IMG SRC=') + 9
    picend = netpage[picstart:].find('''"''') + picstart
    pic = r"http://www.phys.ncku.edu.tw/~astrolab/mirrors/apod/" + netpage[picstart:picend]
    titlestart = netpage.find(r'<b>')
    titleend = netpage.find(r'</b>')
    title = re.sub(r'<.*?>','',re.sub(r'\s*','',netpage[titlestart:titleend]))
    datestart = netpage.find('http://asterisk.apod.com/discuss_apod.php?date=')
    today = netpage[datestart + 47:datestart + 53]
    perurl = r'http://www.phys.ncku.edu.tw/~astrolab/mirrors/apod/ap' + today + '.html'
    desstart = netpage.find(u'說明:')
    desend = netpage[desstart:].find('<p> <center>') + desstart
    description = re.sub(r'<.*?>','',re.sub('[\r\n]*','',netpage[desstart:desend]))
    return '''<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[%s]]></Title> <Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml>''' % (fromu,tou,str(int(time.time())),'APOD' + today + ':' + title,description,pic,perurl)
def caiyun(fromu,tou):
    skycondes = {'CLEAR_DAY':u'晴','CLEAR_NIGHT':u'晴','PARTLY_CLOUDY_DAY':u'多云','PARTLY_CLOUDY_NIGHT':u'多云','CLOUDY':u'阴','RAIN':u'雨','SLEET':u'雨夹雪','SNOW':u'雪','WIND':u'大风','FOG':u'雾霾'}
    caiyunurl = "http://caiyunapp.com/fcgi-bin/v1/api.py?lonlat=117.1783,39.1093&format=json&product=minutes_prec&token=IlaKlDMmXblxGXok"
    caiyunhtml = urllib2.urlopen(caiyunurl).read()
    caiyunjson = json.JSONDecoder().decode(caiyunhtml)
    desnow = caiyunjson['descript_now']
    skycon = skycondes[caiyunjson['skycon']]
    if desnow=='':
        desnow=u'无'
    tempnow = caiyunjson['temp']
    if str(tempnow) in ('','-273'):
        tempnow=u'无法获取'
    summary = caiyunjson['summary']
    if summary=='':
        summary=u'无法获取'
    if skycon=='':
        skycon=u'无法获取'
    timenow = caiyunjson['server_time']
    timestr = time.strftime('%Y%m%d%H%M%S%w',time.localtime(timenow))
    weekname = (u'星期日',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六')
    timechn = timestr[0:4]+u'年'+timestr[4:6]+u'月'+timestr[6:8]+u'日'+weekname[int(timestr[14:])]+' '+timestr[8:10]+u'时'+timestr[10:12]+u'分'+timestr[12:14]+u'秒'
    caiyunstr=u'当前时间：'+timechn+u'。当前天气：'+skycon+u'，当前降水情况：'+desnow+u'，当前温度：'+str(tempnow)+u'摄氏度。未来一小时天气展望：'+summary
    caiyunresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),caiyunstr)
    return caiyunresponse
def weathercn(fromu,tou):
    date = str(time.strftime('%Y%m%d%H%M'))
    retype = 'forecast3d'
    aeraid = '101030100'
    appid = '1464a87405868a90'
    private_key = '3555c3_SmartWeatherAPI_a42779b'
    authurl = 'http://open.weather.com.cn/data/?areaid=%s&type=%s&date=%s&appid=%s' %(aeraid,retype,date,appid)
    key = base64.b64encode(hmac.new(private_key,authurl,hashlib.sha1).digest())
    requesturl = 'http://open.weather.com.cn/data/?areaid=%s&type=%s&date=%s&appid=%s&key=%s' %(aeraid,retype,date,appid[0:6],urllib.quote_plus(key))
    weatherjson = json.loads(urllib.urlopen(requesturl).read())['f']
    weatherdesp = {u'00':u'晴',u'01':u'多云',u'02':u'阴',u'03':u'阵雨',u'04':u'雷阵雨',u'05':u'雷阵雨伴有冰雹',u'06':u'雨夹雪',u'07':u'小雨',u'08':u'中雨',u'09':u'大雨',u'10':u'暴雨',u'11':u'大暴雨',u'12':u'特大暴雨',u'13':u'阵雪',u'14':u'小雪',u'15':u'中雪',u'16':u'大雪',u'17':u'暴雪',u'18':u'雾',u'19':u'冻雨',u'20':u'沙尘暴',u'21':u'小到中雨',u'22':u'中到大雨',u'23':u'大到暴雨',u'24':u'暴雨到大暴雨',u'25':u'大暴雨到特大暴雨',u'26':u'小到中雪',u'27':u'中到大雪',u'28':u'大到暴雪',u'29':u'浮尘',u'30':u'扬沙',u'31':u'强沙尘暴',u'53':u'霾',u'99':u'无'}
    winddir = {u'0':u'无持续风向',u'1':u'东北风',u'2':u'东风',u'3':u'东南风',u'4':u'南风',u'5':u'西南风',u'6':u'西风',u'7':u'西北风',u'8':u'北风',u'9':u'旋转风'}
    windlev = {u'0':u'微风',u'1':u'3-4级',u'2':u'4-5级',u'3':u'5-6级',u'4':u'6-7级',u'5':u'7-8级',u'6':u'8-9级',u'7':u'9-10级',u'8':u'10-11级',u'9':u'11-12级'}
    pubtime = weatherjson['f0']
    pubdate = datetime.date(int(pubtime[0:4]),int(pubtime[4:6]),int(pubtime[6:8]))
    pubtimestr = pubtime[0:8]+' '+pubtime[8:10]+':'+pubtime[10:12]
    weatherstr = []
    for i in range(0,3):
        if weatherjson['f1'][i]['fa']==weatherjson['f1'][i]['fb'] or weatherjson['f1'][i]['fa']=='':
            desp = weatherdesp[weatherjson['f1'][i]['fb']] #18时的预报没有上午的天气信息。
        else:
            desp = u'%s转%s' %(weatherdesp[weatherjson['f1'][i]['fa']],weatherdesp[weatherjson['f1'][i]['fb']])
        if (weatherjson['f1'][i]['fe']==weatherjson['f1'][i]['ff'] and weatherjson['f1'][i]['fg']==weatherjson['f1'][i]['fh']) or weatherjson['f1'][i]['fe']=='':
            dirlev = winddir[weatherjson['f1'][i]['ff']]+windlev[weatherjson['f1'][i]['fh']]
        elif weatherjson['f1'][i]['fe']==weatherjson['f1'][i]['ff']:
            dirlev = u'%s%s转%s' %(winddir[weatherjson['f1'][i]['fe']],windlev[weatherjson['f1'][i]['fg']],windlev[weatherjson['f1'][i]['fh']])
        elif weatherjson['f1'][i]['fg']==weatherjson['f1'][i]['fh']:
            dirlev = u'%s转%s%s' %(winddir[weatherjson['f1'][i]['fe']],winddir[weatherjson['f1'][i]['ff']],windlev[weatherjson['f1'][i]['fg']])
        else:
            dirlev = u'%s%s转%s%s' %(winddir[weatherjson['f1'][i]['fe']],windlev[weatherjson['f1'][i]['fg']],winddir[weatherjson['f1'][i]['ff']],windlev[weatherjson['f1'][i]['fh']])
        datechn = [u'今天',u'明天',u'后天']
        cdate = pubdate+datetime.timedelta(i)
        datedesp = datechn[i]+u'(%s' %(cdate.strftime('%d'))+u'日)'
        if weatherjson['f1'][i]['fc']=='':
            temperature = weatherjson['f1'][i]['fd']
        else:
            temperature = weatherjson['f1'][i]['fd']+'-'+weatherjson['f1'][i]['fc']
        tempstr = u"%s：%s，气温：%s摄氏度，风向风力：%s。日出日落时间：%s。" %(datedesp,desp,temperature,dirlev,weatherjson['f1'][i]['fi']) 
        weatherstr.append(tempstr)
    forecaststr = u'%s\n%s\n%s\n发布时间：%s' %(weatherstr[0],weatherstr[1],weatherstr[2],pubtimestr)
    retype = 'index'
    authurl = 'http://open.weather.com.cn/data/?areaid=%s&type=%s&date=%s&appid=%s' %(aeraid,retype,date,appid)
    key = base64.b64encode(hmac.new(private_key,authurl,hashlib.sha1).digest())
    requesturl = 'http://open.weather.com.cn/data/?areaid=%s&type=%s&date=%s&appid=%s&key=%s' %(aeraid,retype,date,appid[0:6],urllib.quote_plus(key))
    indexjson = json.loads(urllib.urlopen(requesturl).read())['i'][0]
    indexstr = u'今日穿衣指数：%s。%s\n' %(indexjson['i4'],indexjson['i5'])
    respstr = indexstr+forecaststr
    weathercnresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),respstr)
    return weathercnresponse
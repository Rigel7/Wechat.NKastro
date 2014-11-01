# -*- coding: utf-8 -*-
import time,random
from prop import apod,caiyun,weathercn
def selrep(fromu,tou,content):  #fromu和tou是接受的原始xml中指的，回复时对调
    content=content.encode('utf-8')
    if (content=="帮助" or content.startswith("我愿意")):  #帮助
        weekname = (u'星期日',u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六')
        timestr = time.strftime('%Y%m%d%H%M%S%w',time.localtime(time.time()))
        timechn = timestr[0:4]+u'年'+timestr[4:6]+u'月'+timestr[6:8]+u'日'+weekname[int(timestr[14:])]+' '+timestr[8:10]+u'时'+timestr[10:12]+u'分'+timestr[12:14]+u'秒'
        helpcontent = u"现在时间："+timechn+u",欢迎来到南开天协～\n请回复对应编号获取相关信息：\n1.关于我们\n2.查看近期活动\n3.查看近期天象\n4.查看以老图半月坛为地点的晴天钟天文天气预报\n5.查看晴天钟帮助\n6.NASA每日天文一图(APOD)国立成功大学天文实验室镜像\n7.彩云天气二主楼附近当前天气及一小时降雨展望\n8.老图半月坛Heavens-Above人造卫星过境预报\n9.中国天气网天津市区三天天气预报及穿衣指数\n如需人工回复，请以“小南南”开头后跟要说的话。回复“帮助”查看本消息。\n我们还将继续添加更多功能，敬请期待"
        helpresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),helpcontent)
        return helpresponse
    elif (content.startswith("不愿意") or content.startswith("我不愿意")or content.startswith("就不愿意")):
        unwillcontent = "小南南好伤心啊｡ﾟ(ﾟ´ω`ﾟ)ﾟ｡再给你一次说“我愿意”的机会！"
        unwillresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),unwillcontent)
        return unwillresponse
    elif content.startswith("小北北"):
        beibeicontent = "那是小南南的好朋友～"
        beibeiresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),beibeicontent)
        return beibeiresponse
    elif content.startswith("喵"):
        mewcontent = "喵～"
        mewresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),mewcontent)
        return mewresponse
    elif content=="1": #关于我们
        aboutcontent="南开大学天文协会是科普与学术并重的科技类社团。自成立以来，南开大学天文协会已走过18年的风雨历程。从曾经的漠河日全食到现在的路边天文夜，名师讲座，大学生天文节，天文协会已经逐渐趋于成熟。协会秉承“传播天文知识，普及天文科学”的宗旨，为不同层次的天文爱好者搭建了一个了解天文，参与天文观测的平台。同时，我们也鼓励会员参与科普活动，把自己的天文知识和对天文的热爱与大家共享。我们组织的活动被各地天文学家和爱好者认可，也屡次受到媒体的关注。协会的活动是丰富多彩的。你将有机会站在巨人的肩膀上，听大师们讲述宇宙起源和地外文明；或沐浴着清凉的风仰望银河，数着流星划过；或屏住呼吸触摸星空，让思绪穿过望远镜飞到千万年之外；或与我们一同钻研和创造，尽情施展你的才华……不论你是有若干年积淀的资深达人，还是仅仅是喜欢看星星的初级爱好者，天文协会永远是我们共同的家。喜欢星空，就加入我们吧！请回复2查看我们近期的活动信息。"
        aboutresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),aboutcontent)
        return aboutresponse 
    elif content=="2": #近期活动
#        recentactdescription = "大家好~相信很多人已经从新闻中看到了关于10月8日会有月全食发生的信息，小南南也会带大家一起看哒！"
#        recentacttitle = "10月8日和小南南一起看月食~"
#        recentactpic = "http://nkastro.sinaapp.com/static/lunar_eclipse.jpg"
#        recentacturl = "http://mp.weixin.qq.com/s?__biz=MzA4NzAwNDEyMg==&mid=201140388&idx=1&sn=d5ef65b0e15e9ecdb31b7255be075cd6#rd"
#        recentactresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[%s]]></Title> <Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml> " % (fromu,tou,str(int(time.time())),recentacttitle,recentactdescription,recentactpic,recentacturl)
        recentactcontent="各位天文协会的会员们，在上一周的天文科普讲座中，我们认识了四季星空~而在本周六下午两点，我们将讲诉坐标系与望远镜的知识，以及美丽的梅西耶天体的故事~周六下午本部主楼340教室等你来~"
        recentactresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),recentactcontent)
        return recentactresponse
    elif content=="3": #近期天象
        recenteventdescription = "零度星系撰写的2014年10月天象预报。请点击查看原文。"
        recenteventpic = "http://nkastro.sinaapp.com/static/recentevent.jpg"
        recenteventurl = "http://blog.sina.cn/dpool/blog/s/blog_6bcabf350101fqjk.html"
        recenteventresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[近期天象]]></Title> <Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml> " % (fromu,tou,str(int(time.time())),recenteventdescription,recenteventpic,recenteventurl)
        return recenteventresponse
    elif content=="4": #晴天钟预报
        timerurl = "http://202.127.24.18/v4/bin/astro.php?lon=117.1%s&lat=39.1%s&ac=0&lang=zh-CN&unit=metric&tzshift=0" %(str(random.randint(75,85)),str(random.randint(10,15)))   #固定url的话预览小图不会自动更新，因此加上随机
        timerdescription="以南开大学八里台校区老图半月坛为地点的晴天钟天文天气预报。回复5获取晴天钟帮助。天气预报结果无法保证完全准确，仅供参考。\n晴天钟是一系列天气预测产品的总称，它们主要提取于美国国家大气海洋局/气候环境预测局(NOAA/NCEP)的“全球预测系统”(Global Forecast System, GFS)数值模式。晴天钟在2005年7月作为国家天文台宇宙驿站服务器的实验产品开始运作，并在2008年及2011年进行了大规模的翻新。目前它由中国科学院上海天文台中国天文科普网提供硬件及网络支持。"
        timerresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[晴天钟预报]]></Title> <Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml> " % (fromu,tou,str(int(time.time())),timerdescription,timerurl,timerurl)
        return timerresponse
    elif content=="5": #晴天钟帮助
        timerhelpurl = "http://nkastro.sinaapp.com/static/timerhelp.jpg"
        timerhelpdescription="晴天钟相关帮助。点开看大图"
        timerhelpresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><![CDATA[晴天钟帮助]]></Title> <Description><![CDATA[%s]]></Description><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml> " % (fromu,tou,str(int(time.time())),timerhelpdescription,timerhelpurl,timerhelpurl)
        return timerhelpresponse
    elif content=="6": #apod
        apodresponse = apod(fromu,tou)
        return apodresponse 
    elif content=="7": #彩云天气
        caiyunresponse = caiyun(fromu,tou)
        return caiyunresponse
    elif content=="8": #人卫过境
        heavenurls = {'iss':'http://www.heavens-above.com/PassSummary.aspx?satid=25544&lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST','irdium':'http://www.heavens-above.com/IridiumFlares.aspx?lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST','tiangong1':'http://www.heavens-above.com/PassSummary.aspx?satid=37820&lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST','hubble':'http://www.heavens-above.com/PassSummary.aspx?satid=20580&lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST','x37b':'http://www.heavens-above.com/PassSummary.aspx?satid=39025&lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST','bright':'http://www.heavens-above.com/AllSats.aspx?lat=39.1009&lng=117.1715&loc=%E5%8D%97%E5%BC%80%E5%A4%A7%E5%AD%A6%E8%80%81%E5%9B%BE%E5%8D%8A%E6%9C%88%E5%9D%9B&alt=8&tz=ChST'}
        heavenpics = {'iss':'http://nkastro.sinaapp.com/static/iss.jpg','irdium':'http://nkastro.sinaapp.com/static/irdium.jpg','tiangong1':'http://nkastro.sinaapp.com/static/tiangong1.jpg','hubble':'http://nkastro.sinaapp.com/static/hubble.jpg','x37b':'http://nkastro.sinaapp.com/static/x37b.jpg','bright':'http://nkastro.sinaapp.com/static/cz2f.jpg'}
        heavenresponse = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[news]]></MsgType><ArticleCount>6</ArticleCount><Articles><item><Title><![CDATA[ISS(国际空间站)过境]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[铱星闪光预报]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[天宫一号过境]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[哈勃空间望远镜过境]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[X-37B空天飞机过境]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item><item><Title><![CDATA[明亮卫星每日预报]]></Title><PicUrl><![CDATA[%s]]></PicUrl><Url><![CDATA[%s]]></Url></item></Articles></xml>" %(fromu,tou,str(int(time.time())),heavenpics['iss'],heavenurls['iss'],heavenpics['irdium'],heavenurls['irdium'],heavenpics['tiangong1'],heavenurls['tiangong1'],heavenpics['hubble'],heavenurls['hubble'],heavenpics['x37b'],heavenurls['x37b'],heavenpics['bright'],heavenurls['bright'])
        return heavenresponse
    elif content=="9": #中国天气网
        weathercnresponse = weathercn(fromu,tou)
        return weathercnresponse
    elif content.startswith("小南南"): #人工回复
        mancontent="小南南收到啦！我们会尽快回复～"
        manresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),mancontent)
        return manresponse
    else:  #无法识别
        unknowncontent="你说的话小南南听不懂哎...请回复“帮助”获取帮助。如果需要人工回复，请以“小南南”开头发送信息。" 
        unknownresponse="<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content></xml>" %(fromu,tou,str(int(time.time())),unknowncontent)
        return unknownresponse
# -*- coding:utf8 -*- 
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import json
import time
import urllib2
from nova_weixin.config import TEMPLATE_ID
import get_acc_token


# 以下是用于南京大学交换生网站的预留接口
# def send_exchange_template_msg(mes_url,template_id = config.TEMPLATE_ID, title='这里是标题', touser='hahhh'):
#     acc_token = get_acc_token.get_token()
#     ISOTIMEFORMAT='%Y-%m-%d %X'
#     now = time.strftime(ISOTIMEFORMAT, time.localtime())
#     url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % acc_token
#     data = {
#            "touser": '%s' % touser,
#            "template_id": "%s" % template_id,
#            "topcolor": "#FF0000",
#            "url": "%s" % mes_url,
#            "data": {
#                    "first": {
#                        "value": "交换生网站首页通知更新啦！",
#                        "color": "#173177"
#                    },
#                    "keyword1": {
#                        "value": "%s" % title,
#                        "color": "#173177"
#                    },
#                    "keyword2": {
#                        "value": "%s" % now,
#                        "color": "#173177"
#                    },
#                    "remark": {
#                        "value": "请在校园网登陆交换生网站查看详情！",
#                        "color": "#FF8C00"
#                    }
#            }
#        }
#     request = urllib2.urlopen(url, json.dumps(data, ensure_ascii=False))
#     return json.loads(request.read())

def send_common_template_msg(mes_url, template_id=TEMPLATE_ID, title='这里是标题', touser='o19fSvhseI04YpNJkVYVIBTEjESs'):
    acc_token = get_acc_token.get_token()
    ISOTIMEFORMAT='%Y-%m-%d %X'
    now = time.strftime(ISOTIMEFORMAT, time.localtime())
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % acc_token
    data = {
           "touser": '%s' % touser,
           "template_id": "%s" % template_id,
           "topcolor": "#FF0000",
           "url": "%s" % mes_url,
           "data": {
                   "first": {
                       "value": "订阅成功通知！",
                       "color": "#173177"
                   },
                   "keyword1": {
                       "value": "%s" % title,
                       "color": "#173177"
                   },
                   "keyword2": {
                       "value": "%s" % now,
                       "color": "#173177"
                   },
                   "remark": {
                       "value": "欲知详情请点我！",
                       "color": "#FF8C00"
                   }
           }
       }
    request = urllib2.urlopen(url, json.dumps(data, ensure_ascii=False))
    return json.loads(request.read())
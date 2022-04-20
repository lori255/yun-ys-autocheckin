# -*- coding: utf8 -*-
import requests
import json

# 企业微信id
def send_message_QiYeVX(_message, useridlist = ['']): # 默认发送给自己
    useridstr = "|".join(useridlist)
    # 企业微信agentid
    agentid = '###'
    # 企业微信corpid
    corpid = '###'
    # 企业微信corpsecret
    corpsecret = '###'
    response = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    data = json.loads(response.text)
    access_token = data['access_token']

    json_dict = {
       "touser" : useridstr,
       "msgtype" : "text",
       "agentid" : agentid,
       "text" : {
           "content" : _message
       },
       "safe": 0,
       "enable_id_trans": 0,
       "enable_duplicate_check": 0,
       "duplicate_check_interval": 1800
    }
    json_str = json.dumps(json_dict)
    response_send = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}", data=json_str)
    return json.loads(response_send.text)['errmsg'] == 'ok'

# 登录函数
def login(payload):
    url = "https://hk4e-sdk.mihoyo.com/hk4e_cn/combo/granter/login/v2/login"
    headers = {
        'Host': 'hk4e-sdk.mihoyo.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9',
        'Content-Type': 'application/json;charset=utf-8',
        'x-rpc-app_version': '1.3.0',
        'x-rpc-channel_id': '1',
        'x-rpc-device_id': 'cabff8e2d07260e3',
        'x-rpc-device_name': 'Netease MuMu',
        'x-rpc-device_model': 'MuMu',
        'x-rpc-mdk_version': '1.23.0.1',
        'platform': 'true',
        'x-rpc-client_type': '8'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

# 获取云原神账号信息
def get_info(combo_token):
    url = "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/wallet/wallet/get"
    headers = {
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9',
        'x-rpc-app_version': '1.3.0',
        'x-rpc-channel': 'mihoyo',
        'x-rpc-device_id': '27efea83-3030-3921-8203-5e1d91b28e30',
        'x-rpc-device_name': 'Netease MuMu',
        'x-rpc-device_model': 'MuMu',
        'x-rpc-client_type': '2',
        'x-rpc-combo_token': 'ai=4;ci=1;oi=71651386;ct={};si=f89b89f58051050a7b84665636aea1fc0528c1c467c6786860330599c3550807;bi=hk4e_cn'.format(combo_token),
        'x-rpc-sys_version': '6.0.1'
    }
    response = requests.request("GET", url, headers=headers)
    return response.text


def getNotification(combo_token):
    url = "https://api-cloudgame.mihoyo.com/hk4e_cg_cn/gamer/api/listNotifications?status=NotificationStatusUnread&type=NotificationTypePopup&is_sort=true"
    payload = {}
    headers = {
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9',
        'x-rpc-app_version': '1.3.0',
        'x-rpc-channel': 'mihoyo',
        'x-rpc-device_id': '27efea83-3030-3921-8203-5e1d91b28e30',
        'x-rpc-device_name': 'Netease MuMu',
        'x-rpc-device_model': 'MuMu',
        'x-rpc-client_type': '2',
        'x-rpc-combo_token': 'ai=4;ci=1;oi=71651386;ct={};si=f89b89f58051050a7b84665636aea1fc0528c1c467c6786860330599c3550807;bi=hk4e_cn'.format(combo_token),
        'x-rpc-sys_version': '6.0.1',
        'Referer': 'https://app.mihoyo.com'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def batch():
    url = "https://minor-api.mihoyo.com/common/h5log/log/batch?topic=plat_cloudgame"
    payload = "{\"data\":\"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\"}"
    headers = {
        'Referer': 'https://app.mihoyo.com',
        'Host': 'minor-api.mihoyo.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.9',
        'Content-Type': 'application/json; charset=utf-8'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

# 云函数主函数， 需要替换login中的payload
def main_handler(str1, str2):
    # 从云原神抓包获取，替换掉###
    payload = "{\"device\":\"###\",\"app_id\":4,\"channel_id\":1,\"sign\":\"###\",\"data\":\"{\\\"uid\\\":\\\"###\\\",\\\"token\\\":\\\"###\\\",\\\"guest\\\":false}\"}"
    login_info = json.loads(login(payload))
    if login_info['retcode'] != 0:
        print('登录失败！')
    else:
        combo_token = login_info['data']['combo_token']
        batch_info = json.loads(batch())
        user_info = json.loads(get_info(combo_token))
        notification_info = json.loads(getNotification(combo_token))
        print(combo_token)
        print(batch_info)
        print(user_info)
        print(notification_info)
        if notification_info['retcode'] != 0:
            send_message_QiYeVX('{}\n{}'.format('云原神签到失败：', notification_info['message']))
        else:
            send_message_QiYeVX('{}{}\n{}{}'.format('云原神签到：', notification_info['message'], '剩余免费时间(分钟)：', user_info['data']['free_time']['free_time']))

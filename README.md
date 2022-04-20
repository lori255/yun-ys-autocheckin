# yun-ys-autocheckin
云原神自动签到
### 需要一定手机app抓包经验，可以在电脑上下载安卓模拟器，模拟器中安装云原神，再使用fiddler抓包，抓取登录时的payload，替换main_handle的payload
### 如果需要企业微信推送的话，需要在 send_message_QiYeVX 函数中填写相关内容
···python
# 接收消息的人的id userlist，多个人可以用","隔开
userlist = ['XXX']
# 企业微信agentid
agentid = '###'
# 企业微信corpid
corpid = '###'
# 企业微信corpsecret
corpsecret = '###'
```

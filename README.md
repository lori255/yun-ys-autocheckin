# yun-ys-autocheckin
云原神自动签到
### 需要一定手机app抓包经验，可以在电脑上下载安卓模拟器，模拟器中安装云原神，再使用fiddler抓包，抓取登录时的payload，替换main_handle的payload
```python
# 从云原神抓包获取，格式类似下面的示例
payload = "{\"device\":\"###\",\"app_id\":4,\"channel_id\":1,\"sign\":\"###\",\"data\":\"{\\\"uid\\\":\\\"###\\\",\\\"token\\\":\\\"###\\\",\\\"guest\\\":false}\"}"
```
### 如果需要企业微信推送的话，需要在 send_message_QiYeVX 函数中填写相关内容
```python
# 接收消息的人的id userlist，多个人可以用","隔开
userlist = ['XXX']
# 企业微信agentid
agentid = '###'
# 企业微信corpid
corpid = '###'
# 企业微信corpsecret
corpsecret = '###'
```
#### 将main.py中的代码上传腾讯云函数，设置触发器，填写cron表达式，不要填错，会疯狂调用，可能会超出免费额度
#### 我的cron表达式（每天晚上18：30执行一次）：```xml 0 30 18 * * * *```

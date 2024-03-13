#  quanmsms_Python

[中文] | [English](./README.en.md)
#### 介绍
python版本要求:py3.x
安装：pip install quanmsms
最近更新:2023/12/24


#### 使用
```python

# 我们在sdk中提供了example.py(最小示例文件)
# 但您仍可参考本文档
# 请确认在当前环境安装了最新版sdk：pip install quanmsms

from quanmsms import sdk
# openID、Apikey以及模板都可以在 https://dev.quanmwl.com/ability_sms 查看到
# 其中，模板可以在测试接口成功后申请自定义模板
sms = sdk.SDK(
    '2',  # OpenID
    'wd4wa8d4a98w94d89wefwsef4ae9f7ad59ae46s7te49g7t4g9y65h' # Apikey
)
#                        手机号      模板id   模板参数
sendOK, info, apiStatus = sms.send('19954761564', 0, {'code': 12344})
print(sendOK) # 是否成功(布尔值)
print(apiStatus) # api状态码
print(info) # 描述信息 
```
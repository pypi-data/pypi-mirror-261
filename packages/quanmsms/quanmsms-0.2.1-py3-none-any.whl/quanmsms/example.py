# This is a Example file，Creat at 2023/12/10
# python: py3.x[all]
# install this sdk:pip install quanmsms
from quanmsms import sdk

if __name__ == '__main__':
    # openID和Apikey可以在 https://dev.quanmwl.com/ability_sms 查看到
    # 其中，模板可以在测试接口成功后申请自定义模板
    # 本SDK可同时用于sms接口和smspro接口，下面分别进行演示

    # ✨【用于SMS接口的演示】✨
    sms = sdk.SDK(
        '2',  # OpenID【必填】
        '906c98620d8401eea4bf18c05d8c7a9c', # Apikey【必填】
        'http',  # 请求协议【可选：http、https，默认http】
        'sms'  # 客户端类型【可选：sms、smspro，默认sms】
    )
    # 【SMS下基础使用】
    # #                     手机号      模板id//smspro中，这里是短信内容   模板参数
    # sendOK, info, apiStatus = sms.send('19954761564', 0, {'code': 12344})
    # print(sendOK) # 是否成功(布尔值)
    # print(info) # 描述信息
    # print(apiStatus) # 接口响应状态码
    # 【SMS下高级使用】
       #                     手机号      模板id//smspro中，这里是短信内容   模板参数
    res = sms.send_raw('19954761564', 0, {'code': 12344})
    print('状态码：', res.get_code())
    parsetype, raw = res.get_mess()
    print(f'mess: {raw},可以使用{parsetype}格式解析这段消息')
    print('请求id: ', res.get_request_id())
    print('接口余额: ', res.get_residue())

    # ✨【用于SMSPro接口的演示】✨
    smspro = sdk.SDK(
        '2',  # OpenID【必填】
        '906c98620d8401eea4bf18c05d8c7a9c', # Apikey【必填】
        'http',  # 请求协议【可选：http、https，默认http】
        'smspro'  # 客户端类型【可选：sms、smspro，默认sms】
    )
    # 【SMSPro下基础使用】
    # #                     手机号      模板id//smspro中，这里是短信内容   模板参数
    # sendOK, info, apiStatus = sms.send('19954761564', '【泉鸣网络】您的验证码为25271，请勿泄露', {})
    # print(sendOK) # 是否成功(布尔值)
    # print(info) # 描述信息
    # print(apiStatus) # 接口响应状态码
    # 【SMSPro下高级使用】
       #                     手机号      模板id//smspro中，这里是短信内容   模板参数
    res = smspro.send_raw('19954761564', '【泉鸣网络】您的验证码为25271，请勿泄露', {})
    print('状态码：', res.get_code())
    parsetype, raw = res.get_mess()
    print(f'mess: {raw},可以使用{parsetype}格式解析这段消息')
    print('请求id: ', res.get_request_id())
    print('接口余额: ', res.get_residue())

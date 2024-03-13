# -*- coding: utf-8 -*-
# author:Tiper(邱鹏)
# 文件所属项目:QDC SMS SDK
# 文件描述:QuanmSMS SDK (泉鸣开放平台sms接口SDK)，包含执行短信业务所需的方法
# ♥Python版本要求：Python3及以上（可自行修改兼容Python2）♥
# 官网：dev.quanmwl.com
# 更新日期:2024-3-10【融合smsPro接口】

from typing import List, Dict, Tuple
import hashlib
import requests
import json

apis = ["sms", "smspro"]


# SDKError
class SDKError(Exception):
    def __init__(self, message):
        self.message = '[SMS_SDK]' + message


# ApiResponse
class ApiResponse:
    def __init__(self) -> None:
        self.parseType = 'json'
        self.statusCode = ''
        self.mess = None
        self.requestId = ''
        self.residue = 0

    def get_code(self, t='str') -> any:
        """
        获取响应状态码
        :param t: 默认返回str，可指定为int
        :return:
        """
        if t == 'int':
            return int(self.statusCode)
        return self.statusCode

    def get_mess(self) -> Tuple[str, str]:
        """
        获取处理后mess
        :return: [处理格式， 信息原文]
        """
        return self.parseType, self.mess

    def get_request_id(self) -> str:
        """
        获取请求id
        :return:
        """
        return self.requestId

    def get_residue(self) -> int:
        """
        获取接口额度
        :return:
        """
        return self.residue


# SDK class
class SDK:
    def __init__(self, openID='', apiKey='', apiHttp='http', clientType='sms', needRequestId=False):
        # 请开发者修改下列三行配置信息
        self.open_id = openID   # 开发者ID
        self.api_key = apiKey   # 能力列表的apiKey
        self.def_model_id = 0    # 默认情况下使用的模板ID,供外部使用
        self.sdk_version = '0.2.1'  # sdk版本号【非必要不要修改】
        self.need_request_id = needRequestId  # 是否需要请求id
        self.parse_type = 'json'
        if clientType not in apis:
            raise SDKError("ArgerError!clientType must:" + str(apis))
        self.client_type = clientType
        if openID == '' or apiKey == '' :
            raise SDKError("ArgerError!openID or apiKey is null! console:https://dev.quanmwl.com/console")
        if apiHttp != 'http' and apiHttp != 'https':
            raise SDKError("ArgerError!apiHttp:The specified value is not supported!(you can use: 'http' or 'https')")

        # 因备用通道现仅在特殊情况开放【默认关闭】
        # 故自动节点功能默认关闭，不建议普通用户或在未和平台确认的情况下开启自动节点功能
        self.api_http = apiHttp  # 【默认，api支持https，如有需要请修改初始化参数：apiHttp】
        self.api_host = 'dev.quanmwl.com'  # Api Host【默认,非必要无需修改】
        self.api_gateway = self.api_http + '://' + self.api_host  # 【默认,非必要无需修改】

        self.try_next = 0  # 失败容错及刷间隔【默认，非必要无需修改】
        self.standby_number = 0  # 备用线路计数器

        # 更多状态：https://quanmwl.yuque.com/docs/share/9fbd5429-6575-403d-8a3d-7081b2977eda?#8sz4 《平台状态码处理指引》

    def sign(self, _tel, model_id, model_args):
        # type:(str, str, str) -> str
        """
        签名方法
        :param _tel: 接收者手机号
        :param model_id: 短信模板ID
        :param model_args: 短信模板变量参数字典
        :return:
        """
        hl = hashlib.md5()
        server_sign_data = f"{self.open_id}{self.api_key}{_tel}{model_id}{model_args}"
        hl.update(server_sign_data.encode("utf-8"))
        return hl.hexdigest()

    def send(self, tel, model_id, model_args, details=False):
        # type:(str, int, dict, bool) -> tuple[bool, str, str]
        """
        发送短信
        :param tel: 接收者手机号
        :param model_id: 短信模板ID,smspro中表示短信内容
        :param model_args: 短信模板变量参数字典
        :param details: 是否返回详情,不建议用户使用，该设置可能导致第二返回值出现意外的结果，如果需要请求id等详细返回信息，建议使用send_raw方法
        :return:
        """
        headers = {
            'User-Agent': 'QuanmOpenApi_Python_SDK-Sms_' + self.sdk_version,  # 非必要，但推荐传入用于兼容性统计
        }
        api_path = '/v1/sms'

        if self.client_type == 'sms':
            data = {
                'openID': self.open_id,
                'tel': tel,
                'sign': self.sign(tel, str(model_id), str(model_args).replace(' ', '')),
                'model_id': model_id,
                'model_args': f'{model_args}'
            }
        elif self.client_type == 'smspro':
            api_path = '/v1/smspro'
            data = {
                'openID': self.open_id,
                'tel': tel,
                'sign': self.sign(tel, str(model_id), ''),
                'content': model_id
            }
        else:
            raise SDKError('clientType can not use!')

        try:
            response = requests.post(f'{self.api_gateway}{api_path}', headers=headers, data=data)
            http_status = response.status_code
        except:
            self.parse_type = 'string'
            return False, 'Server Error\nTip: You can check if the connection to dev.quanmwl.com is smooth (the gateway you configured is: ' + self.api_gateway +' )If the configuration is correct and the network is unobstructed, please upgrade your SDK', None
        _mess = 'Not Find'
        if response is None or '<!DOCTYPE html>' in response.text:
            print("[SMS_SDK]Requests Fail")
            self.parse_type = 'html'
            if details:
                return False, response.text, None
            return False, _mess, None
        else:
            self.parse_type = 'string'
            try:
                redata = eval(response.text)
            except Exception as e:
                if details:
                    self.parse_type = 'html'
                    return False, response.text, None
                return False, f"解析错误:{e}", None
            else:
                if http_status != 200 or redata is None or redata == {}:
                    return False, 'Rejected:The server refused to process your request,http code:' + str(http_status), None
                _mess = redata['mess']

            self.parse_type = 'json'
            if 'state' not in redata:
                if details:
                    return False, response.text, None
                return False, _mess, None

            api_state = redata['state']
            if api_state == '200':
                
                if details:
                    return False, response.text, api_state
                return True, _mess, api_state
            else:
                if details:
                    return False, response.text, api_state
                return False, _mess, api_state

    def send_raw(self, tel, model_id, model_args) -> ApiResponse:
        """
        发送短信并且返回详情
        :param tel: 接收者手机号
        :param model_id: 短信模板ID,smspro中表示短信内容
        :param model_args: 短信模板变量参数字典
        :return:
        """
        tf, details, code = self.send(tel, model_id, model_args, True)
        response = ApiResponse()
        response.parseType = self.parse_type
        response.mess = str(details)
        response.statusCode = str(code)
        if tf and self.parse_type == 'json':
            raw = json.loaders(details)
            response.requestId = raw.get('request_id', '')
            response.residue = raw.get('residue', 0)
            return response
        return response

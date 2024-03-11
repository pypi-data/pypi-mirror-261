from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name = "quanmsms",
    version = "0.2.0",
    packages=find_packages(),
    description="发送短信,dev.quanmwl.com/ability_sms --> Python版SDK",
    url="https://gitee.com/chengdu-quanming-network/quanmsms-python",
    author="wubie",
    author_email="qp@quanmwl.com",
    long_description = long_description,
    long_description_content_type = "text/markdown"
)
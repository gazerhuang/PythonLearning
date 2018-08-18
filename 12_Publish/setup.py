from distutils.core import setup

setup(name="gz_message",  # 包名
      version="1.0",  # 版本
      description="gazer's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="gazer",  # 作者
      author_email="1@2.c",  # 作者邮箱
      url="www.baidu.com",  # 主页
      py_modules=["gz_message.send_message",
                  "gz_message.receive_message"])

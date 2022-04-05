import json

import grpc
from proto import captcha_pb2
from proto import captcha_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')

    # 调用 rpc 服务
    stub = captcha_pb2_grpc.ServerCaptchaStub(channel)

    # 发送创建创建验证码请求
    # response = stub.Create(captcha_pb2.CreateRequest(ctype="digit"))
    # print("创建验证码：" + response.id, response.question)

    # 发送验证码校验请求
    response = stub.Verify(captcha_pb2.VerifyRequest(
        id="CVNOakVxACydM1HT8j77",
        ctype="digit",
        answer="8198"
    ))
    print("校验验证码：", response.status)


if __name__ == '__main__':
    run()
